import math
import complex

value_int = 33
value_str = "Vasya"
simple_dict = {"Name": "Dima", "age": [1, 5], "eye color": "Green"}
set_obj = {4, 5, 8, 6, 2.12, 3j + 5, 5, None}


def foo(arr, rev=False):
    a = 10
    s = 0
    d = {"Dima": 12, "Vasya": 15}
    for x in arr:
        s += x
    return s + a + num + g, sorted(arr), d


num = 999
g = 1000


class Car:
    color = "Green"
    width = 15

    def __init__(self, speed, marka, weight):
        self.weight = weight
        self.speed = speed
        self.marka = marka

    def calc_time(self, s, name="Dima"):
        t = s / self.speed
        arr = [1, 2, 3, 4, 5]
        sum_arr = sum(arr)
        return t, len(name), sum_arr

    def get_car_color(self):
        return self.color


c = 42


def f(x, y):
    return math.sin(x * y * c)
