from JsonSerializer import JsonSerializer


class Factory:
    @staticmethod
    def setSerializer(serializer_name):
        if serializer_name == "json":
            return JsonSerializer
