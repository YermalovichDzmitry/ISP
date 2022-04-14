from DictSerializer.DictSerializer import DictSerializer
from Serializer.Serializer import Serializer
from Parsers.Parsers import yaml_parser_1
import yaml


class YamlSerializer:
    @staticmethod
    def dump(obj, filename):
        dict_obj = DictSerializer.serialize(obj)
        with open(filename, "w") as f:
            yaml.dump(dict_obj, f)

    @staticmethod
    def dumps(obj):
        dict_obj = DictSerializer.serialize(obj)
        return yaml.dump(dict_obj)

    @staticmethod
    def loads(obj):
        d = yaml.safe_load(obj)
        return DictSerializer.deserialize(d)

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            dict_obj = yaml.safe_load(f)
        return DictSerializer.deserialize(dict_obj)

# class YamlSerializer:
#     @staticmethod
#     def dump(obj, filename):
#         dict_obj = DictSerializer.serialize(obj)
#         yaml_parser_1(dict_obj, 0, filename)
#         obj_tuple_ser = Serializer.serialize(obj)
#
#         str_tuple = Serializer.tuple_to_str(obj_tuple_ser)
#         tuple_filename = filename + "_tuple.txt"
#         with open(tuple_filename, "w") as f:
#             f.write(str_tuple)
#
#     @staticmethod
#     def dumps(obj):
#         dict_obj = DictSerializer.serialize(obj)
#         filename = "../data_for_dumps.txt"
#         yaml_parser_1(dict_obj, 0, filename)
#
#         with open(filename, "r") as f:
#             yaml_ser = f.read()
#         return yaml_ser, dict_obj
#
#     @staticmethod
#     def loads(obj):
#         return DictSerializer.deserialize(obj)
#
#     @staticmethod
#     def load(filename):
#         tuple_filename = filename + "_tuple.txt"
#         with open(tuple_filename, "r") as f:
#             str_obj = f.read()
#         tuple_obj = Serializer.str_to_tuple(str_obj)
#         return Serializer.deserialize(tuple_obj)