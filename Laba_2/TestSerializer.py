import unittest
from TestData import value_int, value_str, simple_dict, foo, Car, f
from Serializer.Serializer import Serializer


def serialize_and_deserialize_obj(obj):
    serialized_object = Serializer.serialize(obj)
    deserialized_object = Serializer.deserialize(serialized_object)
    return deserialized_object


class TestSerializer(unittest.TestCase):
    def test_base_type(self):
        base_objs = [value_int, value_str, simple_dict]
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
