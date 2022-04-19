from Serializer.Serializer import Serializer
from DictSerializer.DictSerializer import DictSerializer
import regex as re
from Arguments.Arguments import file_arg


class JsonSerializer:
    @staticmethod
    def dump(obj, filename):
        obj_dict_ser = DictSerializer.serialize(obj)
        obj_tuple_ser = Serializer.serialize(obj)
        str_tuple = Serializer.tuple_to_str(obj_tuple_ser)

        with open(filename, "w") as f:
            str_sir_json = str(obj_dict_ser)
            str_sir_json = re.sub(r"'", "\"", str_sir_json)
            f.write(str_sir_json)

        tuple_filename = filename + file_arg
        with open(tuple_filename, "w") as f:
            f.write(str_tuple)

    @staticmethod
    def dumps(obj):
        return DictSerializer.serialize(obj)

    @staticmethod
    def loads(obj):
        return DictSerializer.deserialize(obj)

    @staticmethod
    def load(filename):
        tuple_filename = filename + file_arg
        with open(tuple_filename, "r") as f:
            str_obj = f.read()

        tuple_obj = Serializer.str_to_tuple(str_obj)
        return Serializer.deserialize(tuple_obj)