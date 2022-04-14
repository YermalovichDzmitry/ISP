from JsonSerializer.JsonSerializer import JsonSerializer
from DictSerializer.DictSerializer import DictSerializer
from TomlSerializer.TomlSerializer import TomlSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from Factory.Factory import Factory
import math

c = 42


def f(x, y):
    return math.sin(x * y * c)


def define_format1(filename):
    try:
        JsonSerializer.load(filename)
        return "json"
    except:
        pass
    try:
        YamlSerializer.load(filename)
        return "yaml"
    except:
        pass
    try:
        TomlSerializer.load(filename)
        return "toml"
    except:
        pass
    return "Not found"

# ser_obj = YamlSerializer.dumps(f)
# d = YamlSerializer.loads(ser_obj)
# print(d(1, 2))
# YamlSerializer.dump(f, "data.txt")

# d = YamlSerializer.load("data.txt")
# d = TomlSerializer.load("data.txt")
# formats = ["json", "toml", "yaml"]
#
#
# def define_format(filename):
#     try:
#         JsonSerializer.load(filename)
#         return "json"
#     except:
#         pass
#     try:
#         YamlSerializer.load(filename)
#         return "yaml"
#     except:
#         pass
#     try:
#         TomlSerializer.load(filename)
#         return "toml"
#     except:
#         pass
#     return "Not found"


# print(define_format("data.txt"))
# print(d(1, 2))
# TomlSerializer.dump(f, "data.txt")
# d = TomlSerializer.load("data.txt")
# func = DictSerializer.deserialize(d)
# print(func(1, 2))
# ser_obj = TomlSerializer.dumps(f)
# func = TomlSerializer.loads(ser_obj)
# print(func(1, 2))
# JsonSerializer.dump(f, "data.txt")
# ser_obj = JsonSerializer.dump(f, "data.txt")
# des_obg = JsonSerializer.load("data.txt")
# print(des_obg(1, 2))
