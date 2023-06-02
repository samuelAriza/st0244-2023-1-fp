class DataType:
    pass

class Var(DataType):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Nat(DataType):
    def __repr__(self):
        return "Nat"

class Bool(DataType):
    def __repr__(self):
        return "Bool"

class FuncType(DataType):
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def __repr__(self):
        return f"({self.s} -> {self.t})"