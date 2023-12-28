import argparse
import json
import os
import pickle
from pathlib import Path
import sqlite3
from tqdm import tqdm
import random

from utils.linking_process import SpiderEncoderV2Preproc
from utils.pretrained_embeddings import GloVe
from utils.datasets.spider import load_tables
# from dataset.process.preprocess_kaggle import gather_questions


def schema_linking_producer(test, train, table, db, dataset_dir, compute_cv_link=True):

    # load data
    test_data = json.load(open(os.path.join(dataset_dir, test)))
    train_data = json.load(open(os.path.join(dataset_dir, train)))

    # load schemas
    schemas, _ = load_tables([os.path.join(dataset_dir, table)])

    # Backup in-memory copies of all the DBs and create the live connections
    for db_id, schema in tqdm(schemas.items(), desc="DB connections"):
        sqlite_path = Path(dataset_dir) / db / db_id / f"{db_id}.sqlite"
        source: sqlite3.Connection
        with sqlite3.connect(str(sqlite_path)) as source:
            dest = sqlite3.connect(':memory:')
            dest.row_factory = sqlite3.Row
            source.backup(dest)
        schema.connection = dest

    word_emb = GloVe(kind='42B', lemmatize=True)
    linking_processor = SpiderEncoderV2Preproc(dataset_dir,
            min_freq=4,
            max_count=5000,
            include_table_name_in_column=False,
            word_emb=word_emb,
            fix_issue_16_primary_keys=True,
            compute_sc_link=True,
            compute_cv_link=compute_cv_link)

    # build schema-linking
    for data, section in zip([test_data, train_data],['test', 'train']):
        for item in tqdm(data, desc=f"{section} section linking"):
            db_id = item["db_id"]
            schema = schemas[db_id]
            to_add, validation_info = linking_processor.validate_item(item, schema, section)
            if to_add:
                linking_processor.add_item(item, schema, section, validation_info)

    # save
    linking_processor.save()


def bird_pre_process(bird_dir, with_evidence=False):
    new_db_path = os.path.join(bird_dir, "database")
    if not os.path.exists(new_db_path):
        os.system(f"cp -r {os.path.join(bird_dir, 'train/train_databases/*')} {new_db_path}")
        os.system(f"cp -r {os.path.join(bird_dir, 'dev/dev_databases/*')} {new_db_path}")

    def json_preprocess(data_jsons):
        new_datas = []
        for data_json in data_jsons:
            ### Append the evidence to the question
            if with_evidence and len(data_json["evidence"]) > 0:
                data_json['question'] = (data_json['question'] + " " + data_json["evidence"]).strip()
            question = data_json['question']
            tokens = []
            for token in question.split(' '):
                if len(token) == 0:
                    continue
                if token[-1] in ['?', '.', ':', ';', ','] and len(token) > 1:
                    tokens.extend([token[:-1], token[-1:]])
                else:
                    tokens.append(token)
            data_json['question_toks'] = tokens
            data_json['query'] = data_json['SQL']
            new_datas.append(data_json)
        return new_datas

    output_dev = 'dev.json'
    output_train = 'train.json'
    with open(os.path.join(bird_dir, 'dev/dev.json')) as f:
        data_jsons = json.load(f)
        wf = open(os.path.join(bird_dir, output_dev), 'w')
        json.dump(json_preprocess(data_jsons), wf, indent=4)
    with open(os.path.join(bird_dir, 'train/train.json')) as f:
        data_jsons = json.load(f)
        wf = open(os.path.join(bird_dir, output_train), 'w')
        json.dump(json_preprocess(data_jsons), wf, indent=4)
    os.system(f"cp {os.path.join(bird_dir, 'dev/dev.sql')} {bird_dir}")
    os.system(f"cp {os.path.join(bird_dir, 'train/train_gold.sql')} {bird_dir}")
    tables = []
    with open(os.path.join(bird_dir, 'dev/dev_tables.json')) as f:
        tables.extend(json.load(f))
    with open(os.path.join(bird_dir, 'train/train_tables.json')) as f:
        tables.extend(json.load(f))
    with open(os.path.join(bird_dir, 'tables.json'), 'w') as f:
        json.dump(tables, f, indent=4)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="./dataset/spider")
    parser.add_argument("--data_type", type=str, choices=["spider", "bird"], default="spider")
    args = parser.parse_args()

    if data_type == "spider":
        # merge two training split of Spider
        spider_dir = args.data_dir
        split1 = "train_spider.json"
        split2 = "train_others.json"
        total_train = []
        for item in json.load(open(os.path.join(spider_dir, split1))):
            total_train.append(item)
        for item in json.load(open(os.path.join(spider_dir, split2))):
            total_train.append(item)
        with open(os.path.join(spider_dir, 'train_spider_and_others.json'), 'w') as f:
            json.dump(total_train, f)

        # schema-linking between questions and databases for Spider
        spider_dev = "dev.json"
        spider_train = 'train_spider_and_others.json'
        spider_table = 'tables.json'
        spider_db = 'database'
        schema_linking_producer(spider_dev, spider_train, spider_table, spider_db, spider_dir)
    elif data_type == "bird":
        # schema-linking for bird with evidence
        bird_dir = './dataset/bird'
        bird_pre_process(bird_dir, with_evidence=True)
        bird_dev = 'dev.json'
        bird_train = 'train.json'
        bird_table = 'tables.json'
        bird_db = 'databases'
        ## do not compute the cv_link since it is time-consuming in the huge database in BIRD
        schema_linking_producer(bird_dev, bird_train, bird_table, bird_db, bird_dir, compute_cv_link=False)
