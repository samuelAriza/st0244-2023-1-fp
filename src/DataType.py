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

    def __repr__(self, number):
        if(number == 1):
            return self.s
        else:
            return self.t
        
    def __acc__(self, number):
        if(number == 1):
            return f'{self.s}'
        else:
            return f'{self.t}'

    def __str__(self):
        return f"({self.s} -> {self.t})"