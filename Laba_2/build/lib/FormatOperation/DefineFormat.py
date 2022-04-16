from JsonSerializer import JsonSerializer
from YamlSerializer.YamlSerializer import YamlSerializer
from TomlSerializer.TomlSerializer import TomlSerializer


def define_format(filename):
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

    try:
        TomlSerializer.load(filename)
        return "toml"
    except:
        pass
    return "Not found"
