import json

from Serializer import Serializer
import regex as re
import inspect
import json


def serialize_json(obj) -> str:
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{serialize_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""


obj = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
obj_ser = Serializer.serialize(obj)
# obj_ser = f"\"{str(obj_ser)}\""
print(obj_ser)
# with open("data.txt", "w") as f:
#     f.write(json.dumps(obj))
# with open("data.txt", "r") as f:
#     data = f.read()
# print(data)
# obj = set([1, 1, 6, 8, 6, 5, 2, 1, 4, 8])
# print(obj)
# obj_serialize = Serializer.serialize(obj)
# print(obj_serialize)
# obj_deserialize = Serializer.deserialize(obj_serialize)
# print(type(obj_deserialize))

# class Car:
#     color = "Green"
#     width = 15
#
#     def get_car_color(self):
#         return self.color
#
#
# audi = Car()
# ser_obj = Serializer.serialize(audi)
# deser_class = Serializer.deserialize(ser_obj)
# print(deser_class.width)
# ser_obj = Serializer.serialize(Car)
# deser_class = Serializer.deserialize(ser_obj)
# car = deser_class()
# print(car.get_car_color())
#
# class Car:
#     color = "Green"
#     width = 15
#
#     def __init__(self, speed, marka, weight):
#         self.weight = weight
#         self.speed = speed
#         self.marka = marka
#
#     def calc_time(self, s, name="Dima"):
#         t = s / self.speed
#         arr = [1, 2, 3, 4, 5]
#         sum_arr = sum(arr)
#         return t, len(name), sum_arr
#
#     def get_car_color(self):
#         return self.color
#
#
# def foo(a):
#     return a + 10
#
# ser_class=Serializer.serialize(Car)
# Serializer.deserialize(ser_class)
# audi = Car(120, "audi", 4500)
# audi.color = "White"
# print(Serializer.serialize(foo))
# obj_ser = Serializer.serialize(audi)
# obj_dezerialized = Serializer.deserialize(obj_ser)
# print(obj_dezerialized.speed)
# class Car:
#     color = "Green"
#
#     def __init__(self, speed, name="Dima"):
#         self.speed = speed
#
#     def calc_time(self, s):
#         t = s / self.speed
#         return t
#
#     def get_car_color(self):
#         return self.color
#
#
#
# serialized_class = Serializer.serialize(Car)
# NewCar = Serializer.deserialize(serialized_class)
# bmw = NewCar(120)
# print(bmw.get_car_color())
# print(bmw.calc_time(245))
# def foo(arr, rev=False):
#     a = 10
#     arr.append(num)
#     arr_sum = sum(arr) + a
#     return sorted(arr, reverse=rev), arr_sum
#
#
# def foo(arr, rev=False):
#     a = 10
#     s = 0
#     for x in arr:
#         s += x
#     return s + a + num + g, sorted(arr)
#
#
# num = 999
# g = 1000
# print(foo([1, 5, 3, 4, 2]))
# print(Serializer.serialize(foo))
# d = Serializer.serialize(foo)
# func = Serializer.deserialize(d)
# print(func([1, 2, 3, 4, 5], True))
# print(type(d["value"]["__name__"]))
#
# arr = [6, 4, 2, 8, 9, 5, 3]
# print(foo(arr))
# arg = inspect.getmembers(foo)
# value = arg[4][1]
# print(inspect.getmembers(value))
# print(type(arg[4][1]))
# print(foo.__getattribute__("__globals__"))
# d = {"Name": "Dima", "age": [1, 5], "eye color": "Green"}
# bytes_data = "Байты".encode("utf-8")
# b = bytearray(b'hello world!')
# obj = Serializer.serialize(bytes_data)
# print(obj)
#
# arr = [6, 3, [4, 1], 12.34, 76, (1, 2, 3), d, True, complex(3, 4), bytes_data, {1, 5, 3, 1}, None, b]
# print(f"{d}\n")
# obj = Serializer.serialize(d)
# print(f"{obj}\n")
# arr_des = Serializer.deserialize(obj)
# print(arr_des)
