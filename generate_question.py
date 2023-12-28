"""
Generate questions for LLMs and save it as a task
"""
import argparse
import os
import sys
import json
from prompt.prompt_builder import prompt_factory
from utils.data_builder import load_data
from utils.enums import REPR_TYPE, EXAMPLE_TYPE, SELECTOR_TYPE, LLM
from utils.utils import cost_estimate

from tqdm import tqdm

PATH_DATA = "dataset/"

sys.path.append("./")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_type", type=str, choices=["spider", "realistic", "bird"], default="spider")
    parser.add_argument("--split", type=str, choices=["train", "test"], default="test",  required=True)
    parser.add_argument("--k_shot", type=int, default=0, help="Number of examples")
    parser.add_argument("--prompt_repr", type=str, choices=[REPR_TYPE.CODE_REPRESENTATION,
                                                            REPR_TYPE.TEXT_REPRESENTATION,
                                                            REPR_TYPE.OPENAI_DEMOSTRATION,
                                                            REPR_TYPE.BASIC,
                                                            REPR_TYPE.ALPACA_SFT,
                                                            REPR_TYPE.OPENAI_DEMOSTRATION_WFK,
                                                            REPR_TYPE.BASIC_WOFK,
                                                            REPR_TYPE.TEXT_REPRESENTATION_WFK,
                                                            REPR_TYPE.ALPACA_SFT_WFK,
                                                            REPR_TYPE.OPENAI_DEMOSTRATION_WORULE,
                                                            REPR_TYPE.CODE_REPRESENTATION_WRULE,
                                                            REPR_TYPE.ALPACA_SFT_WRULE,
                                                            REPR_TYPE.TEXT_REPRESENTATION_WRULE,
                                                            REPR_TYPE.CODE_REPRESENTATION_COT,
                                                            REPR_TYPE.TEXT_REPRESENTATION_COT,
                                                            REPR_TYPE.OPENAI_DEMOSTRATION_COT,
                                                            REPR_TYPE.ALPACA_SFT_COT,
                                                            REPR_TYPE.CBR])
    parser.add_argument("--example_type", type=str, choices=[EXAMPLE_TYPE.ONLY_SQL, 
                                                             EXAMPLE_TYPE.QA, 
                                                             EXAMPLE_TYPE.COMPLETE,
                                                             EXAMPLE_TYPE.QAWRULE,
                                                             EXAMPLE_TYPE.OPENAI_DEMOSTRATION_QA,
                                                             EXAMPLE_TYPE.BASIC_QA], default=None)
    parser.add_argument("--selector_type", type=str, choices=[SELECTOR_TYPE.COS_SIMILAR,
                                                              SELECTOR_TYPE.RANDOM,
                                                              SELECTOR_TYPE.EUC_DISTANCE,
                                                              SELECTOR_TYPE.EUC_DISTANCE_THRESHOLD,
                                                              SELECTOR_TYPE.EUC_DISTANCE_SKELETON_SIMILARITY_THRESHOLD,
                                                              SELECTOR_TYPE.EUC_DISTANCE_QUESTION_MASK,
                                                              SELECTOR_TYPE.EUC_DISTANCE_PRE_SKELETON_SIMILARITY_THRESHOLD,
                                                              SELECTOR_TYPE.EUC_DISTANCE_PRE_SKELETON_SIMILARITY_PLUS,
                                                              SELECTOR_TYPE.EUC_DISTANCE_MASK_PRE_SKELETON_SIMILARITY_THRESHOLD,
                                                              SELECTOR_TYPE.EUC_DISTANCE_MASK_PRE_SKELETON_SIMILARITY_THRESHOLD_SHIFT
                                                              ], default=None)
    parser.add_argument("--max_seq_len", type=int, default=2048, help="The maximal length that LLM takes")
    parser.add_argument("--max_ans_len", type=int, default=200, help="The maximal length that an answer takes")
    parser.add_argument("--tokenizer", type=str, default="gpt-3.5-turbo")
    parser.add_argument("--scope_factor", type=int, default=100, help="Times of the searching scope")
    parser.add_argument("--pre_test_result", type=str, default=None)

    args = parser.parse_args()

    # load test dataset here
    data = load_data(args.data_type, PATH_DATA, args.pre_test_result)

    # Read all tables into a dict
    databases = data.get_databases()

    # select the prompt
    prompt = prompt_factory(args.prompt_repr, args.k_shot, args.example_type, args.selector_type)(data=data, tokenizer=args.tokenizer)

    # format all questions
    questions = list()
    token_cnt = 0

    # choose split
    func_name = f"get_{args.split}_json"
    cross_domain = args.split == "train"
    
    for question_json in tqdm(getattr(data, func_name)()):
        
        question_format = prompt.format(target=question_json,
                                        max_seq_len=args.max_seq_len,
                                        max_ans_len=args.max_ans_len,
                                        scope_factor=args.scope_factor,
                                        cross_domain=cross_domain)
        
        questions.append(question_format)
        
        token_cnt += question_format["prompt_tokens"]

    # cost estimated
    token_cnt = float(token_cnt) / len(questions)
    print(f"Total {len(questions)} questions, {token_cnt} tokens per prompt, {token_cnt / len(questions)} tokens per question")
    
    n_total_tokens = len(questions) * args.max_ans_len + token_cnt
    cost_gpt_35_turbo = cost_estimate(n_total_tokens, LLM.GPT_35_TURBO)
    cost_text_davinci_003 = cost_estimate(n_total_tokens, LLM.TEXT_DAVINCI_003)
    example_quality = prompt.get_example_quality()
    # example_quality_each = prompt.get_example_quality_for_each()
    pattern_similarity = prompt.get_pattern_similarity()
    print(f"Example quality: {example_quality}")
    print(f"Estimated cost for {LLM.GPT_4}: {cost_gpt_35_turbo*20}")
    print(f"Estimated cost for {LLM.GPT_35_TURBO}: {cost_gpt_35_turbo}")
    print(f"Estimated cost for {LLM.TEXT_DAVINCI_003}: {cost_text_davinci_003}")

    # save questions
    task = {
        "args": vars(args),
        "costs": {
            "prompt_tokens_per_prompt": token_cnt,
            "gpt-4": cost_gpt_35_turbo*20,
            "gpt-3.5-turbo": cost_gpt_35_turbo,
            "text-davinci-003": cost_text_davinci_003,
            "example_quality": example_quality,
            "pattern_similarity": pattern_similarity,
            # "example_quality_for_each": example_quality_each
        },
        "questions": questions
    }
    
    path_generate = f"dataset/process/{args.data_type.upper()}-{args.split.upper()}_{prompt.name}_CTX-{args.max_ans_len}_ANS-{args.max_seq_len}"
        
    os.makedirs(path_generate, exist_ok=True)
    json.dump(task, open(os.path.join(path_generate, "questions.json"), "w"), indent=4)
    