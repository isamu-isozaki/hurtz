# Hertz
Quality of life tool for English 102 students studying under Professor Robert Watts. The only functionality currently is outputting the words you used and the top 10 most common words.
# How to run
Do
```
git clone https://github.com/isamu-isozaki/hurtz.git
cd hurtz
```
Then
```
pip install -e .
```
Then
```
python -m hertz.main --author_name "Robert Watts" --input_file input.txt --log_top_n --n 10
```
Will run the checklist on input.txt where the author name is Robert Watts. Put text in input.txt. --log_all will log all the words in the checklist.
