from DictSerializer.DictSerializer import DictSerializer
import toml
import tomli


class TomlSerializer:
    @staticmethod
    def dump(obj, filename):
        dict_obj = DictSerializer.serialize(obj)
        with open(filename, "w") as f:
            toml.dump(dict_obj, f)

    @staticmethod
    def dumps(obj):
        dict_obj = DictSerializer.serialize(obj)
        return toml.dumps(dict_obj)

    @staticmethod
    def loads(obj):
        dict_obj = tomli.loads(obj)
        return DictSerializer.deserialize(dict_obj)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as f:
            dict_obj = tomli.load(f)
        return DictSerializer.deserialize(dict_obj)