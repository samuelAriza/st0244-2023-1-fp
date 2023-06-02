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
f = DataType.FuncType(DataType.Bool(), DataType.Bool())
#c = DataType.FuncType(DataType.Var("X"), DataType.Var("X"))
tq = TypeEquation.TypeEquation(DataType.Var("X"), DataType.Nat())
tb = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Var("X"), DataType.Var("X")))
tc = tb = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Nat(), DataType.Var("Y")))

print(v)

print(n)

print(b)

print(f)

print(tq)



'''print(type(v))
print(type(n))
print(type(b))
print(type(f))'''

"""
def unify(constraint):
    if (len(constraint) == 0):
        return []
    else:
        first = constraint[0]
        print(first)
"""
"""
def unify(constraints):
    if len(constraints) == 0:
        return []
    else:
        first = constraints[0]
        rest = constraints[1:]
        if first.S == first.T:
            return unify(rest)
        elif isinstance(first.S, DataType.Var):
            return [(first.S, first.T)] + unify(substitute_all(rest, {first.S.name: first.T}))
        elif isinstance(first.T, DataType.Var):
            return [(first.T, first.S)] + unify(substitute_all(rest, {first.T.name: first.S}))
        elif isinstance(first.S, DataType.FuncType) and isinstance(first.T, DataType.FuncType):
            return unify(rest + [TypeEquation.TypeEquation(first.S.s, first.T.s), TypeEquation.TypeEquation(first.S.t, first.T.t)])
        else:
            raise Exception("Unification failed.")
"""

def unify(constraints):
    if len(constraints) == 0:
        return []
    else:
        first = constraints[0]
        rest = constraints[1:]
        if first.S == first.T:
            print(1)
            return unify(rest)
        elif isinstance(first.S, DataType.Var):
            print(2)
            return [(first.S, first.T)] + unify(substitute_all(rest, {first.S.name: first.T}))
        elif isinstance(first.T, DataType.Var):
            print(3)
            return [(first.T, first.S)] + unify(substitute_all(rest, {first.T.name: first.S}))
        elif isinstance(first.S, DataType.FuncType) and isinstance(first.T, DataType.FuncType):
            print(4)
            return unify(rest + [TypeEquation.TypeEquation(first.S.s, first.T.s), TypeEquation.TypeEquation(first.S.t, first.T.t)])
        else:
            print(5)
            return None
        
        

def substitute_all(constraints, substitutions):
    return [eq.substitute(substitutions) for eq in constraints]


def parse_constraints(file_path):
    constraints = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Eliminar espacios en blanco al inicio y final
            if line:  # Ignorar líneas vacías
                eq_parts = line.split('=')
                if len(eq_parts) == 2:
                    s_str, t_str = eq_parts
                    s = parse_data_type(s_str.strip())  # Convertir la cadena en un objeto DataType
                    t = parse_data_type(t_str.strip())  # Convertir la cadena en un objeto DataType
                    constraint = TypeEquation.TypeEquation(s, t)  # Crear un objeto TypeEquation
                    constraints.append(constraint)
    return constraints

def parse_data_type(type_str):
    if type_str == "Nat":
        return DataType.Nat()
    elif type_str == "Bool":
        return DataType.Bool()
    elif "->" in type_str:
        parts = type_str.split("->")
        if len(parts) == 2:
            s_str, t_str = parts
            s = parse_data_type(s_str.strip())
            t = parse_data_type(t_str.strip())
            return DataType.FuncType(s, t)
    elif type_str.startswith("'"):
        name = type_str[1:]
        return DataType.Var(name)
   

constraints = parse_constraints('test/cs1.txt')
#for constraint in constraints:
 #   print(constraint)

#constraints = [tc]


substitutions = unify(constraints)
if substitutions is None:
    print("The constraint set does not unify.")
else:
    print(substitutions)