from JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer


class Factory:
    @staticmethod
    def setSerializer(serializer_name):
        if serializer_name == "yaml":
            return YamlSerializer

        elif serializer_name == "toml":
            return TomlSerializer

        elif serializer_name == "json":
            return JsonSerializer
