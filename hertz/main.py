from hertz.args import hertz_args_parser
from hertz.bad_words import bad_words
import re

import sys

#player has two modes. Random attack mode and distributed attack mode
def main(args):
    global bad_words
    authorname_placeholder = "authorname"
    arg_parser = hertz_args_parser()
    args, _ = arg_parser.parse_known_args(args)#the openai way
    #convert args to dictionary
    args = vars(args)

    author_name_idx = bad_words.index(authorname_placeholder)
    name = args["author_name"].lower().split()
    bad_words = bad_words[:author_name_idx] + name + bad_words[author_name_idx+1:]
    words_dict = {}
    words_popular_dict = {}
    for i, word in enumerate(bad_words):
        words_dict[word] = "bad"
        words_popular_dict[word] = 0
        if word in name or word == "research":
            words_dict[word] = "good"
    
    with open(args["file_name"], "rb") as f:
        usr_text = f.read()

    usr_text = usr_text.decode("utf-8").lower()
    for word in words_dict:
        instances = re.findall("\s+"+word+"\s+", usr_text)
        if word in name:
            instances = re.findall(word, usr_text)
        words_popular_dict[word] = len(instances)
    if args['log_top_n']:
        print(f"Top {args['n']} words")
        ordered_dict = {k: v for k, v in sorted(words_popular_dict.items(), key=lambda x: x[1])[::-1]}#Thanks https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        i = 0
        for k, v in ordered_dict.items():
            if i >= args['n']:
                break
            print(f"{k}: {v}", end=" ")
            print(words_dict[k])
            i += 1
    if args['log_all']:
        print("All words")
        [print(f"{k}: {v}") for k, v in words_popular_dict.items()]
if __name__ == "__main__":
	main(sys.argv)
