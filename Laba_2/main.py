import argparse
from JsonSerializer.JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer
from DefineFormat import define_format
from Serializer.Serializer import Serializer
from Factory.Factory import Factory


def change_format(cur_format, need_format, filename):
    print(cur_format)
    print(need_format)
    builder_serializer_cur = Factory.setSerializer(cur_format)
    builder_serializer_need = Factory.setSerializer(need_format)
    if cur_format == need_format:
        print("The same formats")
        return 0
    des_obj = builder_serializer_cur.load(filename)
    builder_serializer_need.dump(des_obj, filename)


parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default="None")
parser.add_argument('--format', type=str, default="None")
args = parser.parse_args()

filename = args.filename
need_format = args.format

cur_format = define_format(filename)
change_format(cur_format, need_format, filename)
