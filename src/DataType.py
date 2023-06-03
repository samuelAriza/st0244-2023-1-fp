# Class representing a data type
class DataType:
    pass

# Class representing a variable data type
class Var(DataType):
    def __init__(self, name):
        self.name = name

# Returns a string representation of the variable
    def __repr__(self):
        return self.name

# Class representing the 'Nat' data type
class Nat(DataType):
    def __repr__(self):
        return "Nat"

 # Class representing the 'Bool' data type
class Bool(DataType):
    def __repr__(self):
        return "Bool"

# Class representing a function type
class FuncType(DataType):
    def __init__(self, s, t):
        self.s = s
        self.t = t

# Returns a string representation of the function type
    def __repr__(self, number):
        if(number == 1):
            return self.s
        else:
            return self.t

# Accesses the source or target data type of the function type     
    def __acc__(self, number):
        if(number == 1):
            return f'{self.s}'
        else:
            return f'{self.t}'

# Returns a string representation of the function type
    def __str__(self):
        return f"{self.s} → {self.t}"
