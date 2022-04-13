from DictSerializer.DictSerializer import DictSerializer
from Serializer import Serializer
from Parsers.Parsers import toml_parser_1


class TomlSerializer:
    @staticmethod
    def dump(obj, filename):
        dict_obj = DictSerializer.serialize(obj)
        toml_parser_1(obj, filename)
        obj_tuple_ser = Serializer.serialize(obj)

        str_tuple = Serializer.tuple_to_str(obj_tuple_ser)
        tuple_filename = filename + "_tuple.txt"
        with open(tuple_filename, "w") as f:
            f.write(str_tuple)

    @staticmethod
    def dumps(obj):
        dict_obj = DictSerializer.serialize(obj)
        filename = "../data_for_dumps.txt"
        toml_parser_1(dict_obj, filename)
        with open(filename, "r") as f:
            toml_ser = f.read()

        return toml_ser, dict_obj

    @staticmethod
    def loads(obj):
        return DictSerializer.deserialize(obj)

    @staticmethod
    def load(filename):
        tuple_filename = filename + "_tuple.txt"
        with open(tuple_filename, "r") as f:
            str_obj = f.read()

        tuple_obj = Serializer.str_to_tuple(str_obj)
        return Serializer.deserialize(tuple_obj)
