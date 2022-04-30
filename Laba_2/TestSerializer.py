import unittest
from TestData.TestData import value_int, value_str, simple_dict, foo, Car, f, set_obj
from JsonSerializer.JsonSerializer import JsonSerializer
from DictSerializer.DictSerializer import DictSerializer
import json
import re


def serialize_and_deserialize_obj(obj):
    json_object = JsonSerializer.dumps(obj)
    object = JsonSerializer.loads(json_object)
    return object


class TestSerializer(unittest.TestCase):
    def test_base_type(self):
        base_objs = [value_int, value_str, simple_dict, set_obj]
        for obj in base_objs:
            des_obj = serialize_and_deserialize_obj(obj)
            self.assertEqual(des_obj, obj)

    def test_function(self):
        des_obj = serialize_and_deserialize_obj(foo)
        inputs = [6, 5, 2, 78, 9, 5, 2, 5, 8]
        self.assertEqual(des_obj(inputs), foo(inputs))

    def test_class(self):
        des_obj = serialize_and_deserialize_obj(Car)
        audi_origin = Car(120, "audi", 1500)
        audi_des = des_obj(120, "audi", 1500)
        self.assertEqual(audi_origin.color, audi_des.color)
        self.assertEqual(audi_origin.speed, audi_des.speed)
        self.assertEqual(audi_origin.get_car_color(), audi_des.get_car_color())
        self.assertEqual(audi_origin.calc_time(250), audi_des.calc_time(250))

    def test_instance(self):
        audi_origin = Car(120, "audi", 1500)
        audi_origin.color = "White"
        audi_des = serialize_and_deserialize_obj(audi_origin)
        self.assertEqual(audi_origin.color, audi_des.color)
        self.assertEqual(audi_origin.speed, audi_des.speed)
        self.assertEqual(audi_origin.get_car_color(), audi_des.get_car_color())
        self.assertEqual(audi_origin.calc_time(250), audi_des.calc_time(250))

    def test_butoma(self):
        func = serialize_and_deserialize_obj(f)
        self.assertEqual(func(1, 2), f(1, 2))

    def test_json_parser(self):
        base_objs = [value_int, value_str, simple_dict, set_obj]
        for obj in base_objs:
            json_obj = JsonSerializer.dumps(obj)

            self.assertEqual(json_obj, json.dumps(DictSerializer.serialize(obj)))
            DictSerializer.deserialize(DictSerializer.serialize(obj))

        json_obj = JsonSerializer.dumps(foo)
        self.assertEqual(json_obj, json.dumps(DictSerializer.serialize(foo)))
        DictSerializer.deserialize(DictSerializer.serialize(foo))

        json_obj = JsonSerializer.dumps(Car)
        self.assertEqual(json_obj, json.dumps(DictSerializer.serialize(Car)))
        DictSerializer.deserialize(DictSerializer.serialize(Car))

        json_obj = JsonSerializer.dumps(f)
        self.assertEqual(json_obj, json.dumps(DictSerializer.serialize(f)))
        DictSerializer.deserialize(DictSerializer.serialize(f))

        audi_origin = Car(120, "audi", 1500)
        json_obj = JsonSerializer.dumps(audi_origin)
        self.assertEqual(json_obj, json.dumps(DictSerializer.serialize(audi_origin)))
        DictSerializer.deserialize(DictSerializer.serialize(audi_origin))


test_obj = TestSerializer()
test_obj.test_base_type()
test_obj.test_butoma()
test_obj.test_class()
test_obj.test_instance()
test_obj.test_function()
test_obj.test_json_parser()
