from DictSerializer.DictSerializer import DictSerializer
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