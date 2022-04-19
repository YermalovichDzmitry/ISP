from JsonSerializer.JsonSerializer import JsonSerializer


def foo(arr, rev=False):
    a = 10
    s = 0
    d = {"Dima": 12, "Vasya": 15}
    for x in arr:
        s += x
    return s + a + num + g, sorted(arr), d


num = 999
g = 1000

JsonSerializer.dump(foo, "data.txt")

