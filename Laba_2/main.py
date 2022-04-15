from JsonSerializer.JsonSerializer import JsonSerializer
from TestData import value_int, value_str, simple_dict, foo, Car, f, set_obj
import pprint
import json

json_format, str_json = JsonSerializer.dumps(Car)
# pprint.pprint(json_format)
print(str_json)
print(json.dumps(json_format))
print(str_json == json.dumps(json_format))
