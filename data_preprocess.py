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


def schema_linking_producer(test, train, table, db, dataset_dir):

    # load data
    test_data = json.load(open(os.path.join(dataset_dir, test)))
    train_data = json.load(open(os.path.join(dataset_dir, train)))

    # load schemas
    schemas, eval_foreign_key_maps = load_tables([os.path.join(dataset_dir, table)])

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
            compute_cv_link=True)

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="./dataset/spider")
    args = parser.parse_args()

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


