import argparse
import numpy as np

def arg_parser():#credits to OpenAI!
	"""
	Create an empty argparse.ArgumentParser.
	"""
	import argparse
	return argparse.ArgumentParser(
		description="Hertz",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
def hertz_args_parser():
	parser = arg_parser()
	parser.add_argument('--author_name', type=str, default='Robert Watts', help='The name of the author')
	parser.add_argument('--file_name', type=str, default='input.txt', help='The name of input file')
	parser.add_argument('--log_all', default=False, action='store_true', help='Whether to display all words')
	parser.add_argument('--log_top_n', default=False, action='store_true', help='Whether to log top n')
	parser.add_argument('--n', type=int, default=10, help='Display top n values in log_top_n is true')
	return parser