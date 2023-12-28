import argparse
import json
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dail_output", type=str, default=None)
    parser.add_argument("--bird_dev", type=str, default="dataset/bird/dev/dev.json")
    args = parser.parse_args()
    queries = []
    with open(args.dail_output) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) > 0:
                queries.append(line)
    dev = []
    with open(args.bird_dev) as f:
        dev = json.load(f)
    assert len(dev) > 0
    assert len(dev) == len(queries)
    bird_output = {}
    for (q, d) in zip(queries, dev):
        q = q.split('/*')[0]
        bird_output[str(d["question_id"])] = q + "\t----- bird -----\t" + d["db_id"]
    out_file = args.dail_output.replace(".txt", ".json")
    with open(out_file, "w") as f:
        json.dump(bird_output, f, indent = 4)
