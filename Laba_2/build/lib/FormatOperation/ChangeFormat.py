from Factory.Factory import Factory
import os
from Arguments.Arguments import file_arg


def change_format(cur_format, need_format, filename):
    print(cur_format)
    print(need_format)
    builder_serializer_cur = Factory.setSerializer(cur_format)
    builder_serializer_need = Factory.setSerializer(need_format)
    if cur_format == need_format:
        print("The same formats")
        return 0

    des_obj = builder_serializer_cur.load(filename)
    builder_serializer_need.dump(des_obj, filename)
    if cur_format == "json":
        os.remove(filename + file_arg)
