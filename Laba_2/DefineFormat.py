from JsonSerializer.JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer


def define_format(filename):
    try:
        YamlSerializer.load(filename)
        return "yaml"
    except:
        pass
    try:
        TomlSerializer.load(filename)
        return "toml"
    except:
        pass
    try:
        JsonSerializer.load(filename)
        return "json"
    except:
        pass
    return "Not found"
