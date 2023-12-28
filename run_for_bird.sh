python data_preprocess.py --data_type bird --data_dir ./dataset/bird

python generate_question.py --data_type bird \
--split test --tokenizer gpt-3.5-turbo --prompt_repr SQL \
--selector_type EUCDISQUESTIONMASK --max_seq_len 4096 --k_shot 7 --example_type QA

python ask_llm.py \
--openai_api_key $1 \
--model gpt-4 \
--question ./dataset/process/BIRD-TEST_SQL_7-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-4096/ \
--db_dir ./dataset/bird/databases

python generate_question.py --data_type bird --split test --tokenizer gpt-3.5-turbo \
--prompt_repr SQL --max_seq_len 4096 --k_shot 7 --example_type QA --selector_type EUCDISMASKPRESKLSIMTHR \
--pre_test_result ./dataset/process/BIRD-TEST_SQL_7-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4.txt


python 02_ask_chatgpt.py \
--openai_api_key $1 \
--model gpt-4 \
--question ./dataset/process/BIRD-TEST_SQL_7-SHOT_EUCDISMASKPRESKLSIMTHR_QA-EXAMPLE_CTX-200_ANS-4096/ \
--db_dir ./dataset/bird/databases

python to_bird_output.py --dail_output ./dataset/process/BIRD-TEST_SQL_7-SHOT_EUCDISMASKPRESKLSIMTHR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4.txt

cp ./dataset/process/BIRD-TEST_SQL_7-SHOT_EUCDISMASKPRESKLSIMTHR_QA-EXAMPLE_CTX-200_ANS-4096/RESULTS_MODEL-gpt-4.json ./RESULTS_MODEL-gpt-4.json

