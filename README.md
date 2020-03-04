# Hertz
Quality of life tool for English 102 students studying under Professor Robert Watts. The only functionality currently is outputting the words you used and the top 10 most common words.
# How to run
Do
```
pip install -e .
```
Then
```
python -m hertz.main --author_name "Robert Watts" --input_file input.txt --log_top_n --n 10
```
Will run the checklist on input.txt where the author name is Robert Watts
