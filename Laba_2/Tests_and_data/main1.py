from JsonSerializer.JsonSerializer import JsonSerializer
from DictSerializer.DictSerializer import DictSerializer
from TomlSerializer.TomlSerializer import TomlSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
import math

c = 42


def f(x, y):
    return math.sin(x * y * c)


ser_obj = YamlSerializer.dumps(f)
d = YamlSerializer.loads(ser_obj)
print(d(1, 2))
# YamlSerializer.dump(f, "data.txt")
# d = YamlSerializer.load("data.txt")
# print(d(1, 2))
# TomlSerializer.dump(f, "data.txt")
# d = TomlSerializer.load("data.txt")
# func = DictSerializer.deserialize(d)
# print(func(1, 2))
# ser_obj = TomlSerializer.dumps(f)
# func = TomlSerializer.loads(ser_obj)
# print(func(1, 2))
# ser_obj = JsonSerializer.dump(f, "data.txt")
# des_obg = JsonSerializer.load("data.txt")
# print(des_obg(1, 2))
