# Singleton
class Settings:
    __instance = object

    def __init__(self):
        self.port = 0
        self.host = ""

    @classmethod
    def get_intsance(cls):
        if not isinstance(Settings.__instance, Settings):
            Settings.__instance = Settings()
        return Settings.__instance

# Client
settings = Settings.get_intsance()
# let settings = Setting(); # <- Error

settings.host = "192.168.100.1"
settings.port = 33

settings1 = Settings.get_intsance()
# settings1.port is 33

print(settings.port)
