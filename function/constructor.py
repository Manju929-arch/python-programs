from abc import ABC
class Trial(ABC):
    def __init__(self):
        print("Abstract class construtor executed")

class ImpClass(Trial):
    def __init__(self):
        super().__init__()
        print("Imp class constructor executed ")

i = ImpClass()