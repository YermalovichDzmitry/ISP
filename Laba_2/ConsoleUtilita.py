import argparse
from FormatOperation.DefineFormat import define_format
from FormatOperation.ChangeFormat import change_format

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default="None")
parser.add_argument('--format', type=str, default="None")
args = parser.parse_args()

filename = args.filename
need_format = args.format

cur_format = define_format(filename)
change_format(cur_format, need_format, filename)
