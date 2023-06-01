import DataType 
import TypeEquation
'''

X = Nat
S = X
T = Nat

'''
v = DataType.Var("X")
n = DataType.Nat()
b = DataType.Bool()
f = DataType.FuncType(DataType.Bool(), DataType.Nat())
tq = TypeEquation.TypeEquation(DataType.Var("X"), DataType.Nat())

print(type(v))

print(type(n))

print(type((b)))

print(type(f))

print(type(tq))
print(type(tq.__repr__(2)))


'''print(type(v))
print(type(n))
print(type(b))
print(type(f))'''


def unify(constraint):
    if (len(constraint) == 0):
        return []
    else:
        first = constraint[0]
        print(first)


