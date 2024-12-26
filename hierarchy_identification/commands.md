
## Train the reranker
```bash
python reranking/train.py \
  --train_null \
  --add_goal \
  --use_para_score \
  --model_name deberta \
  --context_length 1 \
  --train_file ./data/gold.rerank.org.t30.train.json \
  --dev_file ./data/gold.rerank.org.t30.dev.json \
  --gold_step_goal_para_score ./data/gold.para.base.all.score \
  --save_path ./model/deberta.reranker.pt \
  --neg_num 29 --bs 1 \
  --mega_bs 4 --val_bs 1 \
  --min_save_ep 0 \
  --epochs 5
```
* `train_file` `dev_file`: data files that have linkable steps with their top-30 retrieved goals from the retriever.
* `train_null`: explicitly train the model to predict *unlinkable* steps (S3.3)
* `add_goal`: add the goal of the step as the context of the step (S3.2)
* `use_para_score`: add the score from the retrieval process when calculating the reranking score (Eq.2)
* `context_length`: add the surrounding steps of the target step. n defines the window size
* `gold_step_goal_para_score`: the file that stores the score between each step and its ground truth goal. Other scores are stored in the data files already

## Run the reranker on all wikiHow steps
```bash
python reranking/inference.py \
--model_path ./model/deberta.reranker.pt \
--test_path ./data/all_wikihow_step_t30goals.json \
--save_path ./data/all.result \
--no_label
```

* `test_path`: all steps and their top-30 retrieved goals. The whole wikiHow contains more than 1M steps, the best practice is to split the test file to multiple slides and run them in parallel.

