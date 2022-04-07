import regex as re
from FunctionsArguments import func_arguments, code_arguments, instance_call_members, method_not_call_members
import inspect
import types


class Serializer:
    @staticmethod
    def serialize(obj):
        obj_type = type(obj)
        body = {}
        if isinstance(obj, (int, str, float, bool, complex, bytes, bytearray)):
            distinguished_type = re.search(r"'(\w+)'", str(obj_type))
            body["type"] = distinguished_type.group(1)
            body["value"] = obj
        elif isinstance(obj, list):
            body["type"] = "list"
            body["value"] = []
            for value in obj:
                dict_value = Serializer.serialize(value)
                body["value"].append(dict_value)
        elif isinstance(obj, tuple):
            body["type"] = "tuple"
            body["value"] = tuple([Serializer.serialize(value) for value in obj])
        elif isinstance(obj, set):
            body["type"] = "set"
            body["value"] = tuple([Serializer.serialize(value) for value in obj])
        elif isinstance(obj, dict):
            body["type"] = "dict"
            body["value"] = {}
            for key, value in obj.items():
                dict_value = Serializer.serialize(value)
                body["value"].update({key: dict_value})
        elif isinstance(obj, type(None)):
            body["type"] = "None"
            body["value"] = None
        elif inspect.isfunction(obj):
            body["type"] = "function"
            body["value"] = {}
            all_arguments = inspect.getmembers(obj)
            code_all_arguments = inspect.getmembers(obj.__code__)
            arguments = [argument for argument in all_arguments if argument[0] in func_arguments]
            code_args = [code_argument for code_argument in code_all_arguments if code_argument[0] in code_arguments]
            for argument in arguments:
                if argument[0] != "__code__":
                    body["value"].update({argument[0]: Serializer.serialize(argument[1])})
                else:
                    body["value"].update({"__code__": {}})
                    for code_arg in code_args:
                        body["value"]["__code__"].update({code_arg[0]: Serializer.serialize(code_arg[1])})

            globs_vals = {}
            globs = obj.__getattribute__("__globals__")
            func_glob_args = obj.__code__.co_names
            for func_glob_arg in func_glob_args:
                if func_glob_arg in globs:
                    globs_vals.update({func_glob_arg: globs[func_glob_arg]})
            globs_vals_serialized = Serializer.serialize(globs_vals)
            body["value"].update({"__globals__": globs_vals_serialized})
        elif inspect.isclass(obj):
            body["type"] = "class"
            body["value"] = {}
            name = Serializer.serialize(obj.__name__)
            body["value"].update({"name": name})
            if len(inspect.getmro(obj)) == 2:
                bases = ()
            else:
                pass
            body["value"].update({"bases": Serializer.serialize(bases)})

            info = inspect.getmembers(obj)
            for k, items in enumerate(info):
                if items[0] == "__dict__":
                    break
            class_body_extend = dict(info[k][1])
            class_body_extend.pop("__dict__")
            class_body_extend.pop("__weakref__")
            class_body_extend_serialized = Serializer.serialize(class_body_extend)
            body["value"].update({"class_body": class_body_extend_serialized})
        elif inspect.ismethod(obj):
            body["type"] = "function"
            body["value"] = {}
            body["value"].update({"__name__": Serializer.serialize(obj.__name__)})
            body["value"].update({"__defaults__": Serializer.serialize(obj.__defaults__)})
            body["value"].update({"__closure__": Serializer.serialize(obj.__closure__)})
            code_all_arguments = inspect.getmembers(obj.__code__)
            code_args = [code_argument for code_argument in code_all_arguments if code_argument[0] in code_arguments]
            body["value"].update({"__code__": {}})
            for code_arg in code_args:
                body["value"]["__code__"].update({code_arg[0]: Serializer.serialize(code_arg[1])})

            globs_vals = {}
            globs = obj.__getattribute__("__globals__")
            func_glob_args = obj.__code__.co_names
            for func_glob_arg in func_glob_args:
                if func_glob_arg in globs:
                    globs_vals.update({func_glob_arg: globs[func_glob_arg]})
            globs_vals_serialized = Serializer.serialize(globs_vals)
            body["value"].update({"__globals__": globs_vals_serialized})

        else:
            body["type"] = "instance"
            body["value"] = {}
            name = str(obj.__class__)
            class_type = re.search(r"[.](\w+)'", name)
            name = class_type.group(1)
            body["value"].update({"name": Serializer.serialize(name)})
            members = inspect.getmembers(obj)
            not_call_members = [i for i in members if not callable(i[1])]
            call_members = [i for i in members if callable(i[1])]
            class_body = {}
            for call_member in call_members:
                if call_member[0] not in instance_call_members:
                    class_body.update({call_member[0]: call_member[1]})
            if not inspect.ismethod(obj.__init__):
                class_body.pop("__init__")
            body["value"].update({"class_body": Serializer.serialize(class_body)})
            bases = ()
            body["value"].update({"bases": Serializer.serialize(bases)})

            if inspect.ismethod(obj.__init__):
                attrs = obj.__init__.__code__.co_varnames
                attrs = list(attrs)
                if len(attrs) > 1:
                    constructor_vars = {}
                    for attr in attrs:
                        if attr != "self":
                            constructor_vars.update({attr: obj.__getattribute__(attr)})
                        body["value"].update({"__init__ attribute": Serializer.serialize(constructor_vars)})
                else:
                    body["value"].update({"__init__ attribute": Serializer.serialize(None)})
            else:
                body["value"].update({"__init__ attribute": Serializer.serialize(None)})
            local_vars = []
            global_vars = []
            body["value"].update({"globals": {}})
            for not_call_member in not_call_members:
                if not_call_member[0] in method_not_call_members:
                    body["value"]["globals"].update({not_call_member[0]: Serializer.serialize(not_call_member[1])})
                    if not_call_member[0] == "__dict__":
                        for key, value in not_call_member[1].items():
                            local_vars.append(key)

            for not_call_member in not_call_members:
                if not_call_member[0] not in method_not_call_members and not_call_member[0] not in local_vars:
                    global_vars.append(not_call_member[0])

            body["value"]["globals"].update({"global_vars": {}})
            body["value"]["globals"].update({"local_vars": {}})
            for global_var in global_vars:
                body["value"]["globals"]["global_vars"].update(
                    {global_var: Serializer.serialize(obj.__getattribute__(global_var))})
            for local_var in local_vars:
                body["value"]["globals"]["local_vars"].update(
                    {local_var: Serializer.serialize(obj.__getattribute__(local_var))})
        return body

    @staticmethod
    def deserialize(body):
        object_type = body.get("type")
        obj = None
        if object_type in ["int", "str", "float", "bool", "complex", "bytes", "bytearray"]:
            obj = body["value"]
        elif object_type == "list":
            obj = []
            for value in body["value"]:
                deserialized_object = Serializer.deserialize(value)
                obj.append(deserialized_object)
        elif object_type == "tuple":
            obj = tuple([Serializer.deserialize(value) for value in body["value"]])
        elif object_type == "set":
            obj = set([Serializer.deserialize(value) for value in body["value"]])
        elif object_type == "dict":
            obj = {}
            for key, value in body["value"].items():
                deserialized_object = Serializer.deserialize(value)
                obj.update({key: deserialized_object})
        elif object_type == "None":
            obj = None
        elif object_type == "function":
            code = [0] * 16
            func = [0] * 4
            for key, value in body["value"]["__code__"].items():
                deserialized_object = Serializer.deserialize(value)
                code[code_arguments.index(key)] = deserialized_object
            code = types.CodeType(*code)
            func[0] = code
            for key, value in body["value"].items():
                if key != "__code__" and key != "__globals__":
                    deserialized_object = Serializer.deserialize(value)
                    func[func_arguments.index(key)] = deserialized_object

            globals_deserialized = Serializer.deserialize(body["value"]["__globals__"])
            globals_deserialized.update({"__builtins__": __builtins__})
            func.insert(1, globals_deserialized)
            func = types.FunctionType(*func)
            obj = func
        elif object_type == "class":
            name = Serializer.deserialize(body["value"]["name"])
            bases = Serializer.deserialize(body["value"]["bases"])
            class_body = Serializer.deserialize(body["value"]["class_body"])
            obj = types.new_class(name, bases=bases, kwds=None, exec_body=lambda ns: ns.update(class_body))
        elif object_type == "instance":
            name = Serializer.deserialize(body["value"]["name"])
            bases = Serializer.deserialize(body["value"]["bases"])
            class_body = Serializer.deserialize(body["value"]["class_body"])

            for method_not_call_member in method_not_call_members:
                if method_not_call_member != "__dict__":
                    class_body.update({method_not_call_member: Serializer.deserialize(
                        body["value"]["globals"][method_not_call_member])})
            if body["value"]["globals"]["global_vars"]:
                for key, value in body["value"]["globals"]["global_vars"].items():
                    class_body.update({key: Serializer.deserialize(value)})
            if body["value"]["globals"]["local_vars"]:
                for key, value in body["value"]["globals"]["local_vars"].items():
                    class_body.update({key: Serializer.deserialize(value)})
            deserialized_class = types.new_class(name, bases=bases, kwds=None,
                                                 exec_body=lambda ns: ns.update(class_body))
            init_attrs = Serializer.deserialize(body["value"]["__init__ attribute"])
            if init_attrs:
                attrs = []
                for init_attr in init_attrs.items():
                    attrs.append(init_attr[1])
                obj = deserialized_class(*attrs)
            else:
                obj = deserialized_class()
        return obj
