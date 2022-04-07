from Serializer import Serializer
import json

class JsonSerializer:
    def dump(self, obj, filename):
        pass

    def dumps(self, obj):
        return Serializer.serialize(obj)

    def loads(self, obj):
        Serializer.deserialize(obj)

    def load(self, obj, filename):
        pass
