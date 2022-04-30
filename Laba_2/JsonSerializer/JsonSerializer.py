from DictSerializer.DictSerializer import DictSerializer
import regex as re
from JsonParser.JsonParser import json_parser


class JsonSerializer:
    @staticmethod
    def dump(obj, filename):
        obj_dict_ser = DictSerializer.serialize(obj)
        with open(filename, "w") as f:
            str_sir_json = str(obj_dict_ser)
            str_sir_json = re.sub(r"'", "\"", str_sir_json)
            f.write(str_sir_json)

    @staticmethod
    def dumps(obj):
        return re.sub(r"'", "\"", str(DictSerializer.serialize(obj)))

    @staticmethod
    def loads(obj):
        return DictSerializer.deserialize(json_parser(obj))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            str_obj = f.read()

        return DictSerializer.deserialize(json_parser(str_obj))
