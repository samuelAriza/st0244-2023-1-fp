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
    elif("→" in datatype_str):
        parts = datatype_str.split('→')
        for i in range(0, len(parts)):
            parts[i] = parse_datatype(parts[i].replace(' ', ''))
        n = 2
        output = [parts[i:i + n] for i in range(0, len(parts), n)]
        
        if(len(output) == 1 and len(output[0]) == 2):
            s = output[0][0]
            t = output[0][1]

        if(len(output) > 1 and len(output[1]) == 2):
            s = DataType.FuncType(output[0][0], output[0][1])
            t = DataType.FuncType(output[1][0], output[1][1])

        if(len(output) > 1 and len(output[1]) == 1):
            s = DataType.FuncType(output[0][0], output[0][1])
            t = output[1][0]

        return DataType.FuncType(s, t)
    

    else:
        return DataType.Var(datatype_str)
#print(parse_type_equation("X → Y = Nat → X").__str__())