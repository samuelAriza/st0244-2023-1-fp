import DataType 
import TypeEquation

# Determines the free variables in a type equation.
def fv(type_equation, d):
    flag = False
    fv = []
    s = type_equation.__repr__(1)
    t = type_equation.__repr__(2)

    # Checks free variables in the target type
    if (d == "t"):
        if (type(t) != DataType.FuncType and type(t) == DataType.Var):
            fv.append(t.__repr__())
        elif(type(t) == DataType.FuncType):
            for i in range(1, 3):
                if(type(t.__repr__(i)) == DataType.Var):
                    fv.append(t.__repr__(i).name)

        # Checks if the source variable is present in the free variables of the target type
        for i in range(0, len(fv)):
            if(s.name == fv[i]):
                flag = True
    else:

        # Checks free variables in the source type.
        if (type(s) != DataType.FuncType and type(s) == DataType.Var):
            fv.append(s.__repr__())
        elif(type(s) == DataType.FuncType):
            for i in range(1, 3):
                if(type(s.__repr__(i)) == DataType.Var):
                    fv.append(s.__repr__(i).name)

        # Checks if the target variable is present in the free variables of the source type.
        for i in range(0, len(fv)):
            if(t.name == fv[i]):
                flag = True
    return flag

# Swaps a variable with its value in a type equation.
def swap(type_equation, variable, value):
    s = type_equation.__repr__(1)
    t = type_equation.__repr__(2)

    # If the source type is a variable and matches the target variable, swap it with the value.
    if(type(s) == DataType.Var and s.name == variable):
        s = value
    elif(type(s) == DataType.FuncType):
        s_ = s.__repr__(1)
        t_ = s.__repr__(2)

        # If the source type is a function type and the first part matches the variable,
        # swap it with the value.
        if(type(s_) == DataType.Var and s_.name == variable):
            s_ = value

        # If the source type is a function type and the second part matches the variable, 
        # swap it with the value.
        if(type(t_) == DataType.Var and t_.name == variable):
            t_ = value
        s = DataType.FuncType(s_, t_)
    
    # If the target type is a variable and matches the source variable, swap it with the value.
    if(type(t) == DataType.Var and t.name == variable):
        t = value
    elif(type(t) == DataType.FuncType):
        s_ = t.__repr__(1)
        t_ = t.__repr__(2)

        # If the target type is a function type and the first part matches the variable,
        # swap it with the value.
        if(type(s_) == DataType.Var and s_.name == variable):
            s_ = value

        # If the target type is a function type and the second part matches the variable,
        # swap it with the value.
        if(type(t_) == DataType.Var and t_.name == variable):
            t_ = value
        t = DataType.FuncType(s_, t_)

    return TypeEquation.TypeEquation(s, t)

# Unifies a set of type equations.
def unify(constraint):
    if (len(constraint) == 0):
        return []
    else:
        first_equation = constraint[0]
        s = first_equation.__repr__(1)
        t = first_equation.__repr__(2)

        # If the source and target types are the same,
        # remove the equation and continue unifying.
        if(s == t):
            constraint.pop(0)
            unify(constraint)

        # If the source type is a variable and not a free variable in the target type, 
        # perform variable substitution.
        elif(type(s) == DataType.Var and fv(first_equation, "t") == False):
            for i in range(0, len(constraint)):
                constraint[i] = swap(constraint[i], s.name, t)
            if(type(t) == DataType.FuncType):
                print(f'{s.name} ⇾ {t.__repr__(1)} → {t.__repr__(2)}')
            else:
                print(f'{s.name} ⇾ {t.__repr__()}')
            constraint.pop(0)
            unify(constraint)

        # If the target type is a variable and not a free variable in the source type,
        # perform variable substitution.
        elif(type(t) == DataType.Var and fv(first_equation, "s") == False):
            for i in range(0, len(constraint)):
                constraint[i] = swap(constraint[i], t.name, s)
            
            if(type(t) == DataType.FuncType):
                print(f'{t.name} → {s.__str__()}')
            else:
                print(f'{t.name} → {s.__repr__()}')
            constraint.pop(0)
            unify(constraint)

        # If both source and target types are function types,
        # split the equation into two separate equations.
        elif(type(s) == DataType.FuncType and type(t) == DataType.FuncType):
            s_ = s.__repr__(1)
            s__ = s.__repr__(2)
            t_ = t.__repr__(1)
            t__ = t.__repr__(2)
            constraint.append(TypeEquation.TypeEquation(s_, t_))
            constraint.append(TypeEquation.TypeEquation(s__, t__))
            constraint.pop(0)
            unify(constraint)

        # If none of the unification conditions are met, 
        # the constraint set cannot be unified.
        else:
            if(type(s) == type(t)):
                constraint.pop(0)
                unify(constraint)
            else:
                print("The constraint set does not unify.")
