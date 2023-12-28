import json
import os

from utils.utils import get_tables, sql2skeleton
from utils.linking_utils.application import get_question_pattern_with_schema_linking


class BasicDataset(object):
    def __init__(self, path_data, pre_test_result=None):
        self.path_data = os.path.join(path_data, self.name)
        self.path_db = os.path.join(self.path_data, "database")
        self.test_json = os.path.join(self.path_data, self.test_json)
        self.test_gold = os.path.join(self.path_data, self.test_gold)
        self.train_json = os.path.join(self.path_data, self.train_json)
        self.train_gold = os.path.join(self.path_data, self.train_gold)
        self.table_json = os.path.join(self.path_data, self.table_json)
        self.path_test_schema_linking = os.path.join(self.path_data, "enc/test_schema-linking.jsonl")
        self.path_train_schema_linking = os.path.join(self.path_data, "enc/train_schema-linking.jsonl")
        if self.mini_test_index_json:
            self.mini_test_index_json = os.path.join(self.path_data, self.mini_test_index_json)
        else:
            self.mini_test_index_json = None

        self.pre_test_result = pre_test_result
            
        # lazy load for tables
        self.databases = None

    # test a mini set
    def set_mini_test(self, mini_file):
        self.mini_test_index_json = os.path.join(self.path_data, mini_file)

    def get_databases(self):
        if self.databases is None:
            self.databases = dict()
            # for db_id in os.listdir(self.path_db):
            #     self.databases[db_id] = self.get_tables(db_id)
            with open(self.table_json) as f:
                tables = json.load(f)
                for tj in tables:
                    db_id = tj["db_id"]
                    self.databases[db_id] = self.get_tables(db_id)
        return self.databases

    def get_tables(self, db_id):
        if db_id in self.databases:
            return self.databases[db_id]
        else:
            path_db = os.path.join(self.path_db, db_id, db_id + ".sqlite")
            tables = get_tables(path_db)
            self.databases[db_id] = tables
            return tables

    def get_path_sql(self, db_id):
        path_sql = os.path.join(self.path_db, db_id, "schema.sql")
        return path_sql
        
    def get_table_json(self):
        return json.load(open(self.table_json, "r"))

    def get_path_db(self, db_id):
        return os.path.join(self.path_db, db_id, f"{db_id}.sqlite")

    def get_train_questions(self):
        questions = json.load(open(self.train_json, "r"))
        return [_["question"] for _ in questions]

    def get_mini_index(self):
        if self.mini_test_index_json:
            return json.load(open(self.mini_test_index_json, "r"))
        else:
            return None

    def get_test_questions(self, mini_set=False):
        questions = json.load(open(self.test_json, "r"))
        if mini_set and self.mini_test_index_json:
            mini_test_index = self.get_mini_index()
            questions = [questions[i] for i in mini_test_index]
        return [_["question"] for _ in questions]

    # get query skeletons
    def get_pre_skeleton(self, queries=None, schemas=None, mini_set=False):
        if queries:
            skeletons = []
            for query,schema in zip(queries, schemas):
                skeletons.append(sql2skeleton(query, schema))
            if mini_set and self.mini_test_index_json:
                mini_index = self.get_mini_index()
                skeletons = [skeletons[i] for i in mini_index]
            return skeletons
        else:
            return False

    # get all train information
    def get_train_json(self):
        datas = json.load(open(self.train_json, "r"))
        linking_infos = self.get_train_schema_linking()
        db_id_to_table_json = dict()
        for table_json in self.get_table_json():
            db_id_to_table_json[table_json["db_id"]] = table_json
        schemas = [db_id_to_table_json[d["db_id"]] for d in datas]
        queries = [data["query"] for data in datas]
        pre_queries = self.get_pre_skeleton(queries, schemas)
        return self.data_pre_process(datas, linking_infos, pre_queries)

    # get all test information
    def get_test_json(self, mini_set=False):
        tests = json.load(open(self.test_json, "r"))
        if mini_set and self.mini_test_index_json:
            mini_test_index = self.get_mini_index()
            tests = [tests[i] for i in mini_test_index]
        linking_infos = self.get_test_schema_linking(mini_set)
        db_id_to_table_json = dict()
        for table_json in self.get_table_json():
            db_id_to_table_json[table_json["db_id"]] = table_json
        schemas = [db_id_to_table_json[d["db_id"]] for d in tests]
        if self.pre_test_result:
            with open(self.pre_test_result, 'r') as f:
                lines = f.readlines()
                queries = [line.strip() for line in lines]
                pre_queries = self.get_pre_skeleton(queries, schemas, mini_set)
        else:
            pre_queries = None
        return self.data_pre_process(tests, linking_infos, pre_queries)

    def get_test_schema_linking(self, mini_set=False):
        if not os.path.exists(self.path_test_schema_linking):
            return None
        linking_infos = []
        with open(self.path_test_schema_linking, 'r') as f:
            for line in f.readlines():
                if line.strip():
                    linking_infos.append(json.loads(line))
        if mini_set and self.mini_test_index_json:
            mini_test_index = self.get_mini_index()
            linking_infos = [linking_infos[i] for i in mini_test_index]
        return linking_infos

    def get_train_schema_linking(self):
        if not os.path.exists(self.path_train_schema_linking):
            return None
        linking_infos = []
        with open(self.path_train_schema_linking, 'r') as f:
            for line in f.readlines():
                if line.strip():
                    linking_infos.append(json.loads(line))
        return linking_infos

    def get_all_json(self):
        return self.get_train_json() + self.get_test_json()

    def get_train_answers(self):
        with open(self.train_gold, "r") as file:
            answers = file.readlines()
            return answers

    def get_test_answers(self, mini_set=False):
        with open(self.test_gold, "r") as file:
            answers = file.readlines()
            if mini_set and self.mini_test_index_json:
                mini_test_index = self.get_mini_index()
                answers = [answers[i] for i in mini_test_index]
            return answers

    def get_train_duplicated_index(self):
        train_data = self.get_train_json()
        example_dict = {}
        duplicated_index = []
        for i in range(len(train_data)):
            db_id = train_data[i]["db_id"]
            question = train_data[i]["question"]
            if (db_id, question) in example_dict.keys():
                duplicated_index.append(i)
            else:
                example_dict[(db_id, question)] = True
        return duplicated_index

    # get skeletons and schema_linking info
    def data_pre_process(self, datas, linking_infos=None, pre_queries=None):
        db_id_to_table_json = dict()
        for table_json in self.get_table_json():
            db_id_to_table_json[table_json["db_id"]] = table_json
        for data in datas:
            db_id = data["db_id"]
            data["tables"] = self.get_tables(db_id)
            if data["query"].strip()[:6] != 'SELECT':
                data["query_skeleton"] = data["query"]
            else:
                data["query_skeleton"] = sql2skeleton(data["query"], db_id_to_table_json[db_id])
            data["path_db"] = self.get_path_db(db_id)
        if linking_infos:
            db_id_to_table_json = dict()
            for table_json in self.get_table_json():
                db_id_to_table_json[table_json["db_id"]] = table_json
            for id in range(min(len(datas), len(linking_infos))):
                datas[id]["sc_link"] = linking_infos[id]["sc_link"]
                datas[id]["cv_link"] = linking_infos[id]["cv_link"]
                datas[id]["question_for_copying"] = linking_infos[id]["question_for_copying"]
                datas[id]["column_to_table"] = linking_infos[id]["column_to_table"]
                db_id = datas[id]["db_id"]
                datas[id]["table_names_original"] = db_id_to_table_json[db_id]["table_names_original"]
            question_patterns = get_question_pattern_with_schema_linking(datas)
            for id in range(len(datas)):
                datas[id]["question_pattern"] = question_patterns[id]
        if pre_queries:
            for id in range(min(len(datas), len(pre_queries))):
                datas[id]["pre_skeleton"] = pre_queries[id]
        return datas


class SpiderDataset(BasicDataset):
    name = "spider"
    test_json = "dev.json"
    test_gold = "dev_gold.sql"
    train_json = "train_spider_and_others.json"
    train_gold = "train_gold.sql"
    table_json = "tables.json"
    mini_test_index_json = "mini_dev_index.json"


class RealisticDataset(BasicDataset):
    # only used for data path, shared with spider
    name = "spider_realistic"
    test_json = "spider-realistic.json"
    test_gold = "spider-realistic_gold.sql"
    train_json = "train_spider_and_others.json"
    train_gold = "train_gold.sql"
    table_json = "tables.json"
    mini_test_index_json = None

class BirdDataset(BasicDataset):
    name = "bird"
    test_json = "dev.json"
    test_gold = "dev.sql"
    train_json = "train.json"
    train_gold = "train_gold.sql"
    table_json = "tables.json"
    mini_test_index_json = None


def load_data(data_type, path_data, pre_test_result=None):
    if data_type.lower() == "spider":
        return SpiderDataset(path_data, pre_test_result)
    elif data_type.lower() == "realistic":
        return RealisticDataset(path_data, pre_test_result)
    elif data_type.lower() == "bird":
        return BirdDataset(path_data, pre_test_result)
    else:
        raise RuntimeError()
