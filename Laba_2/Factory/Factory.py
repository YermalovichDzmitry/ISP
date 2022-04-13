from JsonSerializer.JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer


class Factory:
    @staticmethod
    def setSerializer(serializer_name):
        if serializer_name == "json":
            return JsonSerializer

        if serializer_name == "yaml":
            return YamlSerializer

        if serializer_name == "yaml":
            return TomlSerializer
