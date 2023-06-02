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
f = DataType.FuncType(DataType.Bool(), DataType.Var("Y"))

'''
print(type(v))
print(type(n))
print(type((b)))
print(type(f))
print(type(tq))
print(type(tq.__repr__(2)))
print(type(v))
print(type(n))
print(type(b))
print(type(f))


S = T

x = Nat
'''
variable = DataType.Var("X")

tt = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Var("X"), DataType.Var("X")))

tq = TypeEquation.TypeEquation(v, n)

tf = TypeEquation.TypeEquation(n, v)
nn = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Nat(), DataType.Var("Y")))
ff = TypeEquation.TypeEquation(DataType.FuncType(DataType.Nat(), DataType.Bool()), DataType.FuncType(DataType.Nat(), DataType.Var("X")))


def fv(type_equation, d):
    flag = False
    fv = []
    s = type_equation.__repr__(1)
    t = type_equation.__repr__(2)
    ['x', 'x']

    if (d == "t"):
        if (type(t) != DataType.FuncType and type(t) == DataType.Var):
            fv.append(t.__repr__())
        elif(type(t) == DataType.FuncType):
            for i in range(1, 3):
                if(type(t.__repr__(i)) == DataType.Var):
                    fv.append(t.__repr__(i).name)

        for i in range(0, len(fv)):
            if(s.name == fv[i]):
                flag = True
    else:
        if (type(s) != DataType.FuncType and type(s) == DataType.Var):
            fv.append(s.__repr__())
        elif(type(s) == DataType.FuncType):
            for i in range(1, 3):
                if(type(s.__repr__(i)) == DataType.Var):
                    fv.append(s.__repr__(i).name)

        for i in range(0, len(fv)):
            if(t.name == fv[i]):
                flag = True
    return flag

def swap(type_equation, variable, value):
    s = type_equation.__repr__(1)
    t = type_equation.__repr__(2)

    if(type(s) == DataType.Var and s.name == variable):
        s = value
    elif(type(s) == DataType.FuncType):
        s_ = s.__repr__(1)
        t_ = s.__repr__(2)
        if(type(s_) == DataType.Var and s_.name == variable):
            s_ = value
        if(type(t_) == DataType.Var and t_.name == variable):
            t_ = value
        s = DataType.FuncType(s_, t_)
    
    if(type(t) == DataType.Var and t.name == variable):
        t = value
    elif(type(t) == DataType.FuncType):
        s_ = t.__repr__(1)
        t_ = t.__repr__(2)
        if(type(s_) == DataType.Var and s_.name == variable):
            s_ = value
        if(type(t_) == DataType.Var and t_.name == variable):
            t_ = value
        t = DataType.FuncType(s_, t_)

    return TypeEquation.TypeEquation(s, t)

def unify(constraint):
    if (len(constraint) == 0):
        return []
    else:
        first_equation = constraint[0]
        s = first_equation.__repr__(1)
        t = first_equation.__repr__(2)
        if(s == t):
            constraint.pop(0)
            unify(constraint)
        elif(type(s) == DataType.Var and fv(first_equation, "t") == False):
            for i in range(0, len(constraint)):
                constraint[i] = swap(constraint[i], s.name, t)

            if(type(t) == DataType.FuncType):
                print(f'{s.name} -> {t.__str__()}')
            else:
                print(f'{s.name} -> {t.__repr__()}')
            unify(constraint[1:])
        elif(type(t) == DataType.Var and fv(first_equation, "s") == False):
            for i in range(0, len(constraint)):
                constraint[i] = swap(constraint[i], t.name, s)
            
            if(type(t) == DataType.FuncType):
                print(f'{t.name} -> {s.__str__()}')
            else:
                print(f'{t.name} -> {s.__repr__()}')
            constraint.pop(0)
            unify(constraint[1:])
        elif(type(s) == DataType.FuncType and type(t) == DataType.FuncType):
            s_ = s.__repr__(1)
            s__ = s.__repr__(2)
            t_ = t.__repr__(1)
            t__ = t.__repr__(2)

            constraint.append(TypeEquation.TypeEquation(s_, t_))
            constraint.append(TypeEquation.TypeEquation(s__, t__))
            constraint.pop(0)
            unify(constraint[1:])
        else:
            raise Exception("Unify Fail")

constraints = [nn]
unify(constraints)

