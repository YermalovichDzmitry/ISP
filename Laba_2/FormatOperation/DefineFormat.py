from JsonSerializer.JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer


def define_format(filename):
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

    try:
        YamlSerializer.load(filename)
        return "yaml"
    except:
        pass
    return "Not found"
