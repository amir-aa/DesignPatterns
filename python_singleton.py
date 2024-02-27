class Config:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Config,cls).__new__(cls)
        return cls._instance

    def getConfig(self):
        return {"APIKEY":"1234"}


c1=Config()
c2=Config()
print(c1.getConfig())
print(c2.getConfig())
print("True result indicates that Singleton Works: ", c1 is c2)
