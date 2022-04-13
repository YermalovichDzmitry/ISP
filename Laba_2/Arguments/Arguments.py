func_arguments = ["__code__", "__name__", "__defaults__", "__closure__"]

code_arguments = ["co_argcount", "posonlyargcount", "co_kwonlyargcount", "co_nlocals", "co_stacksize", "co_flags",
                  "co_code", "co_consts", "co_names",
                  "co_varnames", "co_filename", "co_name", "co_firstlineno", "co_lnotab", "co_freevars", "co_cellvars"]

instance_call_members = ["__subclasshook__", "__str__", "__sizeof__", "__setattr__", "__repr__", "__reduce_ex__",
                         "__reduce__", "__new__",
                         "__ne__", "__lt__", "__le__", "__init_subclass__", "__hash__", "__gt__", "__getattribute__",
                         "__ge__", "__format__",
                         "__eq__", "__dir__", "__delattr__", "__class__"]

method_not_call_members = ["__dict__", "__doc__", "__module__", "__weakref__"]
