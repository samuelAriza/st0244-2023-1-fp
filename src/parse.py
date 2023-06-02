import DataType 
import TypeEquation
# →
def parse_type_equation(string):
    parts = string.split('=')
    S = parse_datatype(parts[0].strip())
    T = parse_datatype(parts[1].strip())
    return TypeEquation.TypeEquation(S, T)

def parse_datatype(datatype_str):
    if (datatype_str == "Nat"):
        return DataType.Nat()
    elif (datatype_str == "Bool"):
        return DataType.Bool()
    else:
        try:
            flag = False
            for i in range(0, len(datatype_str)):
                if(datatype_str[i] == "→"):
                    flag = True
            if(flag == True):
                parts = datatype_str.split('→')
                s = parts[0].strip()
                t = parts[1].strip()
                if(s == "Nat"):
                    f = DataType.Nat()
                elif(s == "Bool"):
                    f = DataType.Bool()
                else:
                    f = DataType.Var(s)
                if(t == "Nat"):
                    s = DataType.Nat()
                elif(t == "Bool"):
                    s = DataType.Bool()
                else:
                    s = DataType.Var(s)

                return DataType.FuncType(f, s)
            else:
                raise Exception("Fail")
        except:
            return DataType.Var(datatype_str)

print(parse_type_equation("X → Nat = Bool").__str__())