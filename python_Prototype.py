import copy
class Configuration:
    def __init__(self,apikey:str) -> None:
        self.apikey=apikey
    def clone(self):
        return copy.deepcopy(self) # We Can use copy instead

base_config=Configuration("test2")
c1=base_config.clone()
c1.apikey="testc1"
c2=base_config.clone()
c2.apikey="testc2"
print(c1.__dict__)
print(c2.__dict__)
