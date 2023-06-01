class DataType:
    pass

class Var(DataType):
    def __init__(self, name):
        self.name = name

class Nat(DataType):
    pass

class Bool(DataType):
    pass

class FuncType(DataType):
    def __init__(self, s, t):
        self.s = s
        self.t = t
