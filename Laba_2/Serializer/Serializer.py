import regex as re
from Arguments.Arguments import func_arguments, code_arguments, instance_call_members, method_not_call_members
import inspect
import types


class Serializer:
    @staticmethod
    def serialize(obj):
        obj_type = type(obj)
        body = {}
        if obj_type == int:
            body["type"] = "int"
            body["value"] = obj

        elif obj_type == str:
            body["type"] = "str"
            body["value"] = obj

        elif obj_type == float:
            body["type"] = "float"
            body["value"] = obj

        elif obj_type == bool:
            body["type"] = "bool"
            body["value"] = obj

        elif obj_type == complex:
            body["type"] = "complex"
            body["value"] = obj

        elif obj_type == bytes:
            body["type"] = "bytes"
            body["value"] = tuple([Serializer.serialize(i) for i in obj])

        elif obj_type == list:
            body["type"] = "list"
            body["value"] = tuple([Serializer.serialize(i) for i in obj])

        elif obj_type == tuple:
            body["type"] = "tuple"
            body["value"] = tuple([Serializer.serialize(value) for value in obj])

        elif obj_type == set:
            body["type"] = "set"
            body["value"] = tuple([Serializer.serialize(value) for value in obj])

        elif obj_type == dict:
            body["type"] = "dict"
            body["value"] = {}
            for key, value in obj.items():
                dict_key = Serializer.serialize(key)
                dict_value = Serializer.serialize(value)
                body["value"].update({dict_key: dict_value})
            body["value"] = tuple((key, body["value"][key]) for key in body["value"])

        elif isinstance(obj, type(None)):
            body["type"] = "NoneType"
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
                    body["value"].update({Serializer.serialize(argument[0]): Serializer.serialize(argument[1])})
                else:
                    body["value"].update({Serializer.serialize("__code__"): {}})
                    for code_arg in code_args:
                        body["value"][Serializer.serialize("__code__")].update(
                            {Serializer.serialize(code_arg[0]): Serializer.serialize(code_arg[1])})

            globs_vals = {}
            globs = obj.__getattribute__("__globals__")
            func_glob_args = obj.__code__.co_names
            modules_names = []
            for func_glob_arg in func_glob_args:
                if func_glob_arg in globs:
                    if isinstance(globs[func_glob_arg], types.ModuleType):
                        modules_names.append(func_glob_arg)
                    else:
                        globs_vals.update({func_glob_arg: globs[func_glob_arg]})
            globs_vals.update({"__modules": modules_names})
            globs_vals_serialized = Serializer.serialize(globs_vals)
            body["value"].update({Serializer.serialize("__globals__"): globs_vals_serialized})
            body["value"][Serializer.serialize("__code__")] = tuple(
                (key, body["value"][Serializer.serialize("__code__")][key]) for key in
                body["value"][Serializer.serialize("__code__")])
            body["value"] = tuple((key, body["value"][key]) for key in body["value"])

        elif inspect.isclass(obj):
            body["type"] = "class"
            body["value"] = {}
            name = Serializer.serialize(obj.__name__)
            body["value"].update({Serializer.serialize("name"): name})
            if len(inspect.getmro(obj)) == 2:
                bases = ()
            else:
                pass
            body["value"].update({Serializer.serialize("bases"): Serializer.serialize(bases)})

            info = inspect.getmembers(obj)
            for k, items in enumerate(info):
                if items[0] == "__dict__":
                    break
            class_body_extend = dict(info[k][1])
            class_body_extend.pop("__dict__")
            class_body_extend.pop("__weakref__")
            class_body_extend_serialized = Serializer.serialize(class_body_extend)
            body["value"].update({Serializer.serialize("class_body"): class_body_extend_serialized})
            body["value"] = tuple((k, body["value"][k]) for k in body["value"])

        elif inspect.ismethod(obj):
            body["type"] = "function"
            body["value"] = {}
            body["value"].update({Serializer.serialize("__name__"): Serializer.serialize(obj.__name__)})
            body["value"].update({Serializer.serialize("__defaults__"): Serializer.serialize(obj.__defaults__)})
            body["value"].update({Serializer.serialize("__closure__"): Serializer.serialize(obj.__closure__)})
            code_all_arguments = inspect.getmembers(obj.__code__)
            code_args = [code_argument for code_argument in code_all_arguments if code_argument[0] in code_arguments]
            body["value"].update({Serializer.serialize("__code__"): {}})
            for code_arg in code_args:
                body["value"][Serializer.serialize("__code__")].update(
                    {Serializer.serialize(code_arg[0]): Serializer.serialize(code_arg[1])})

            globs_vals = {}
            globs = obj.__getattribute__("__globals__")
            func_glob_args = obj.__code__.co_names
            for func_glob_arg in func_glob_args:
                if func_glob_arg in globs:
                    globs_vals.update({func_glob_arg: globs[func_glob_arg]})
            globs_vals_serialized = Serializer.serialize(globs_vals)
            body["value"].update({Serializer.serialize("__globals__"): globs_vals_serialized})

            body["value"][Serializer.serialize("__code__")] = tuple(
                (key, body["value"][Serializer.serialize("__code__")][key]) for key in
                body["value"][Serializer.serialize("__code__")])
            body["value"] = tuple((key, body["value"][key]) for key in body["value"])

        else:
            body["type"] = "instance"
            body["value"] = {}
            name = str(obj.__class__)
            class_type = re.search(r"[.](\w+)'", name)
            name = class_type.group(1)
            body["value"].update({Serializer.serialize("name"): Serializer.serialize(name)})
            members = inspect.getmembers(obj)
            not_call_members = [i for i in members if not callable(i[1])]
            call_members = [i for i in members if callable(i[1])]
            class_body = {}
            for call_member in call_members:
                if call_member[0] not in instance_call_members:
                    class_body.update({call_member[0]: call_member[1]})
            if not inspect.ismethod(obj.__init__):
                class_body.pop("__init__")
            body["value"].update({Serializer.serialize("class_body"): Serializer.serialize(class_body)})
            bases = ()
            body["value"].update({Serializer.serialize("bases"): Serializer.serialize(bases)})

            if inspect.ismethod(obj.__init__):
                attrs = obj.__init__.__code__.co_varnames
                attrs = list(attrs)
                if len(attrs) > 1:
                    constructor_vars = {}
                    for attr in attrs:
                        if attr != "self":
                            constructor_vars.update({attr: obj.__getattribute__(attr)})
                        body["value"].update(
                            {Serializer.serialize("__init__ attribute"): Serializer.serialize(constructor_vars)})
                else:
                    body["value"].update({Serializer.serialize("__init__ attribute"): Serializer.serialize(None)})
            else:
                body["value"].update({Serializer.serialize("__init__ attribute"): Serializer.serialize(None)})
            local_vars = []
            global_vars = []
            body["value"].update({Serializer.serialize("globals"): {}})
            for not_call_member in not_call_members:
                if not_call_member[0] in method_not_call_members:
                    body["value"][Serializer.serialize("globals")].update(
                        {Serializer.serialize(not_call_member[0]): Serializer.serialize(not_call_member[1])})
                    if not_call_member[0] == "__dict__":
                        for key, value in not_call_member[1].items():
                            local_vars.append(key)

            for not_call_member in not_call_members:
                if not_call_member[0] not in method_not_call_members and not_call_member[0] not in local_vars:
                    global_vars.append(not_call_member[0])

            global_vars_dict = {}
            local_vars_dict = {}
            for global_var in global_vars:
                global_vars_dict.update(
                    {Serializer.serialize(global_var): Serializer.serialize(obj.__getattribute__(global_var))})
            for local_var in local_vars:
                local_vars_dict.update(
                    {Serializer.serialize(local_var): Serializer.serialize(obj.__getattribute__(local_var))})

            body["value"][Serializer.serialize("globals")].update(
                {Serializer.serialize("global_vars"): Serializer.serialize(global_vars_dict)})
            body["value"][Serializer.serialize("globals")].update(
                {Serializer.serialize("local_vars"): Serializer.serialize(local_vars_dict)})

            body["value"][Serializer.serialize("globals")] = tuple(
                (key, body["value"][Serializer.serialize("globals")][key]) for key in
                body["value"][Serializer.serialize("globals")])

            body["value"] = tuple((key, body["value"][key]) for key in body["value"])

        body = tuple((key, body[key]) for key in body)
        return body

    @staticmethod
    def deserialize(body):
        body = dict((a, b) for a, b in body)
        object_type = body.get("type")
        obj = None
        if object_type == "int":
            obj = int(body["value"])

        elif object_type == "str":
            obj = str(body["value"])

        elif object_type == "float":
            obj = float(body["value"])

        elif object_type == "complex":
            obj = complex(body["value"])

        elif object_type == "bytes":
            obj = bytes([Serializer.deserialize(i) for i in body["value"]])

        elif object_type == "bool":
            obj = body["value"] == "True"

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
            for item in body["value"]:
                val = Serializer.deserialize(item[1])
                obj[Serializer.deserialize(item[0])] = val

        elif object_type == "NoneType":
            obj = None

        elif object_type == "function":
            code = [0] * 16
            func = [0] * 4
            globals_deserialized = {}
            for item in body["value"]:
                key = Serializer.deserialize(item[0])
                if key == "__code__":
                    code_dict = {}
                    for x in item[1]:
                        code_dict.update({Serializer.deserialize(x[0]): Serializer.deserialize(x[1])})
                elif key == "__globals__":
                    globals_deserialized = Serializer.deserialize(item[1])
                    if globals_deserialized["__modules"]:
                        for item in globals_deserialized["__modules"]:
                            globals_deserialized.update({item: __import__(item)})

                    globals_deserialized.update({"__builtins__": __builtins__})
                else:
                    deserialized_object = Serializer.deserialize(item[1])
                    func[func_arguments.index(key)] = deserialized_object
            for key, value in code_dict.items():
                code[code_arguments.index(key)] = value
            code = types.CodeType(*code)
            func[0] = code
            func.insert(1, globals_deserialized)
            func = types.FunctionType(*func)
            obj = func

        elif object_type == "class":
            for item in body["value"]:

                key = Serializer.deserialize(item[0])
                if key == "name":
                    name = Serializer.deserialize(item[1])
                elif key == "bases":
                    bases = Serializer.deserialize(item[1])
                elif key == "class_body":
                    class_body = Serializer.deserialize(item[1])

            obj = types.new_class(name, bases=bases, kwds=None, exec_body=lambda ns: ns.update(class_body))

        elif object_type == "instance":
            for item in body["value"]:

                key = Serializer.deserialize(item[0])
                if key == "name":
                    name = Serializer.deserialize(item[1])
                elif key == "bases":
                    bases = Serializer.deserialize(item[1])
                elif key == "class_body":
                    class_body = Serializer.deserialize(item[1])
                elif key == "__init__ attribute":
                    __init__attribute_dict = Serializer.deserialize(item[1])
                elif key == "globals":
                    globals_dict = {"globals": {}}
                    for x in item[1]:
                        globals_dict["globals"].update({Serializer.deserialize(x[0]): Serializer.deserialize(x[1])})
                    for method_not_call_member in method_not_call_members:
                        if method_not_call_member != "__dict__":
                            class_body.update({method_not_call_member: globals_dict["globals"][method_not_call_member]})

                    if globals_dict["globals"]["global_vars"]:
                        for key, value in globals_dict["globals"]["global_vars"].items():
                            class_body.update({Serializer.deserialize(key): Serializer.deserialize(value)})

                    if globals_dict["globals"]["local_vars"]:
                        for key, value in globals_dict["globals"]["local_vars"].items():
                            class_body.update({Serializer.deserialize(key): Serializer.deserialize(value)})
                    deserialized_class = types.new_class(name, bases=bases, kwds=None,
                                                         exec_body=lambda ns: ns.update(class_body))
                    init_attrs = __init__attribute_dict
                    if init_attrs:
                        attrs = []
                        for init_attr in init_attrs.items():
                            attrs.append(init_attr[1])
                        obj = deserialized_class(*attrs)
                    else:
                        obj = deserialized_class()
        return obj

    @staticmethod
    def tuple_to_str(tuple_object):
        if type(tuple_object) == tuple:
            array_item = []
            for i in tuple_object:
                array_item.append(f"{Serializer.tuple_to_str(i)}")
            tuple_str = ", ".join(array_item)
            return f"[{tuple_str}]"
        else:
            return f"\"{str(tuple_object)}\""

    @staticmethod
    def str_to_tuple(str_obj):
        if str_obj == '[]':
            return tuple()
        elif str_obj[0] == '[':
            str_obj = str_obj[1:len(str_obj) - 1]
            tuple_data = []
            deep = 0
            comma = False
            substr = ""
            for i in str_obj:
                if i == '[':
                    deep += 1
                elif i == ']':
                    deep -= 1
                elif i == '\"':
                    comma = not comma
                elif i == ',' and not comma and deep == 0:
                    tuple_data.append(Serializer.str_to_tuple(substr))
                    substr = ""
                    continue
                elif i == ' ' and not comma:
                    continue

                substr += i

            tuple_data.append(Serializer.str_to_tuple(substr))
            return tuple(tuple_data)
        else:
            return str_obj[1:len(str_obj) - 1]
