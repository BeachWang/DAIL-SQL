echo "data_preprocess"
python data_preprocess.py

echo "generate question with EUCDISQUESTIONMASK"
python generate_question.py \
--data_type spider \
--split test \
--tokenizer gpt-3.5-turbo \
--max_seq_len 10000 \
--prompt_repr SQL \
--k_shot 9 \
--example_type QA \
--selector_type  EUCDISQUESTIONMASK

echo "generate SQL by GPT-4 for EUCDISMASKPRESKLSIMTHR as the pre-generated SQL query"
python ask_llm.py \
--openai_api_key $1  \
--model gpt-4 \
--question ./dataset/process/SPIDER-TEST_SQL_9-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-10000/ \
--n 5 \
--db_dir ./dataset/spider/database \
--temperature 1.0

echo "generate question with EUCDISMASKPRESKLSIMTHR"
python generate_question.py \
--data_type spider \
--split test \
--tokenizer gpt-3.5-turbo \
--max_seq_len 10000 \
--selector_type EUCDISMASKPRESKLSIMTHR \
--pre_test_result ./dataset/process/SPIDER-TEST_SQL_9-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-10000/RESULTS_MODEL-gpt-4.txt \
--prompt_repr SQL \
--k_shot 9 \
--example_type QA

echo "generate SQL by GPT-4 for EUCDISMASKPRESKLSIMTHR"
python ask_llm.py \
--openai_api_key $1  \
--model gpt-4 \
--question ./dataset/process/SPIDER-TEST_SQL_9-SHOT_EUCDISMASKPRESKLSIMTHR_QA-EXAMPLE_CTX-200_ANS-10000/ \
--n 5 \
--db_dir ./dataset/spider/database \
--temperature 1.0