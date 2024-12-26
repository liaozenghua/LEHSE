
### Evaluation
```bash
#ER-1(Goal)
python run.py --mode 2 --test_mode 1
#ER-L(Script)
python run.py --mode 2 --test_mode 2
#ER-L(Step)
python run.py \
  --mode 2 \
  --test_mode 5.1 \
  --step_weight 0.5 \
  --help_version mr
#ER-L(Hypernym)
python run.py \
  --mode 2 \
  --test_mode 5.2 \
  --step_weight 0.5 \
  --help_version mr
```
