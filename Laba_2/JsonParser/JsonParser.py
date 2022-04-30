def simple_parser(str_obj):
    list_data = []
    substr = ""
    k = 0

    for i in str_obj:
        if i == "\"":
            if k == 0:
                k += 1
                continue
            if k == 1:
                list_data.append(substr)
                if len(list_data) == 2:
                    break
                substr = ""
                k = 0
        elif k == 1:
            substr += i
        elif i in [" ", ":"]:
            pass
    return list_data


def list_parser(str_obj):
    deep = 1
    index_start = str_obj.find("[")
    index_fin = index_start
    for i in str_obj[index_start + 1:]:
        if i == "[":
            deep += 1
        elif i == "]":
            deep -= 1
        elif deep == 0:
            break
        index_fin += 1
    list_str = str_obj[index_start + 1:index_fin]
    list_arr = []
    substr = ""
    deep = 0
    for i in list_str:
        if i == "{":
            deep += 1
        elif i == "}":
            deep -= 1

        if deep == 0 and i not in [" ", ","]:
            substr += i
            list_arr.append(substr)
            substr = ""
            continue

        if i not in [" ", ","] or deep >= 1:
            substr += i
    final_list = []
    for item in list_arr:
        final_list.append(json_parser(item))
    return final_list


def dict_parser(str_obj):
    index_start_1 = str_obj.find("{")
    index_end_1 = index_start_1
    deep = 0
    d = {}
    for i in str_obj[index_start_1:]:
        if i == "{":
            deep += 1
        elif i == "}":
            deep -= 1
        if deep == 0:
            index_end_1 += 1
            break
        index_end_1 += 1
    sub_dict = str_obj[index_start_1:index_end_1]
    while len(sub_dict) > 6:
        k = 0
        dict_key = ""
        for i in sub_dict:
            if i == "\"":
                if k == 0:
                    k += 1
                elif k == 1:
                    k = 0
                    break
            elif k == 1:
                dict_key += i
        sub_dict = sub_dict[len(dict_key) + 3:]

        deep = 0
        sub_str = ""
        n = 0
        for i in sub_dict:
            if i == "{":
                deep += 1
                n = 1
            elif i == "}":
                deep -= 1
            if deep == 0 and n != 0:
                sub_str += i
                break
            if deep >= 1:
                sub_str += i
        if dict_key == "__code__":
            d.update({dict_key: dict_parser(sub_str)})
        elif dict_key == "globals":
            d.update({dict_key: dict_parser(sub_str)})
        elif dict_key == "global_vars":
            d.update({dict_key: dict_parser(sub_str)})
        elif dict_key == "local_vars":
            d.update({dict_key: dict_parser(sub_str)})
        else:
            d.update({dict_key: json_parser(sub_str)})

        if len(sub_dict) < len(sub_str) + 4:
            sub_dict = ""
        else:
            sub_dict = sub_dict[len(sub_str) + 4:]

            if sub_dict[0] != "\"":
                sub_dict = "\"" + sub_dict

    return d


def json_parser(str_obj):
    list_data = []
    substr = ""
    k = 0
    index = 0
    d = {}

    for j, i in enumerate(str_obj):
        if i == "\"":
            if k == 0:
                k += 1
                continue
            if k == 1:
                list_data.append(substr)
                if len(list_data) == 2:
                    index = j + 3
                    break
                substr = ""
                k = 0
        elif k == 1:
            substr += i
        elif i in [" ", ":"]:
            pass
    d.update({list_data[0]: list_data[1]})

    if list_data[1] in ["int", "float", "str", "NoneType", "bool", "complex"]:
        value = simple_parser(str_obj[index:])
        d.update({value[0]: value[1]})

    if list_data[1] in ["list", "tuple", "bytes", "set"]:
        ser_list = list_parser(str_obj[index:])
        d.update({"value": ser_list})

    if list_data[1] in ["dict", "function", "class", "instance"]:
        ser_list = dict_parser(str_obj[index:])
        d.update({"value": ser_list})

    return d
