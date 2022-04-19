import regex as re


def yaml_parser_1(object, deep, filename, prev=None):
    object_type = type(object)
    if object_type == int:
        return str(object)

    elif object_type == float:
        return str(object)

    elif object_type == str:
        return str(object)

    elif object_type == bool:
        return str(object)

    elif object_type == complex:
        return str(object)

    elif object_type == type(None):
        return str(None)

    elif object_type == dict:
        for key, value in object.items():
            key_str = yaml_parser_1(key, deep + 1, filename)
            if type(value) == list or type(value) == tuple or type(value) == set or type(value) == bytes:
                if prev == "list":
                    with open(filename, "a") as f:
                        f.write(deep * " " + f"  {key_str}: \n")
                else:
                    with open(filename, "a") as f:
                        f.write(deep * " " + f"{key_str}: \n")
                value_str = yaml_parser_1(value, deep + 1, filename)
            elif type(value) == dict:
                with open(filename, "a") as f:
                    f.write(deep * " " + f"{key_str}: \n")
                yaml_parser_1(value, deep + 1, filename)

            else:
                value_str = yaml_parser_1(value, deep + 1, filename)
                if prev == "list":
                    if key_str == "type":
                        with open(filename, "a") as f:
                            f.write(deep * " " + f"- {key_str}: {value_str}\n")
                    else:
                        with open(filename, "a") as f:
                            f.write(deep * " " + f"  {key_str}: {value_str}\n")
                else:
                    with open(filename, "a") as f:
                        f.write(deep * " " + f"{key_str}: {value_str}\n")
    elif object_type == list or object_type == bytes or object_type == tuple or object_type == set:
        if len(object) == 0:
            yaml_parser_1({"value": "[]"}, deep + 1, filename)

        else:
            for item in object:
                yaml_parser_1(item, deep + 1, filename, "list")
    else:
        return "[]"


def toml_parser_1(object, filename, prev=None, key_obj=None):
    object_type = type(object)
    if object_type == int:
        return str(object)
    elif object_type == float:
        return str(object)
    elif object_type == str:
        object_str = str(object)
        object = re.sub(r"\\", r"\\\\", object_str)
        return str(object)
    elif object_type == bool:
        return str(object)
    elif object_type == complex:
        return str(object)
    elif object_type == type(None):
        return str(None)
    elif object_type == dict:
        k = 0
        for key, value in object.items():
            key_str = toml_parser_1(key, filename)
            if type(value) == list:
                if key_obj is None:
                    pass
                else:
                    key_str = key_str + "." + key_obj

                toml_parser_1(value, filename, key_obj=key_str)
            elif type(value) == dict:
                toml_parser_1(value, filename, key_obj=key_str, prev="dict")
            else:
                if prev == "list":
                    if k == 0:
                        with open(filename, "a") as f:
                            f.write(f"[[{key_obj}]]\n")
                        k += 1
                    else:
                        pass
                    val_str = toml_parser_1(value, filename)
                    with open(filename, "a") as f:
                        f.write(f"{key_str} = \"{val_str}\"\n")

                elif prev == "dict":
                    if k == 0:
                        with open(filename, "a") as f:
                            f.write(f"[{key_obj}]\n")
                        k += 1
                    else:
                        pass
                    val_str = toml_parser_1(value, filename)
                    with open(filename, "a") as f:
                        f.write(f"{key_str} = \"{val_str}\"\n")

                else:
                    val_str = toml_parser_1(value, filename)
                    with open(filename, "a") as f:
                        f.write(f"{key_str} = \"{val_str}\"\n")

    elif object_type == list or object_type == bytes or object_type == tuple or object_type == set:
        for item in object:
            toml_parser_1(item, filename, prev="list", key_obj=key_obj)
            with open(filename, "a") as f:
                f.write(f"\n")

