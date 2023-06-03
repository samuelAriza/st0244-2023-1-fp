import DataType 
import TypeEquation

# → The arrow symbol used in type equations

# Parses a string representation of a type equation
def parse_type_equation(string):
    
    # Split the string representation of the type equation into its left and 
    # right sides
    parts = string.split('=')

    # Parses the data types from the left and right sides of the equation
    S = parse_datatype(parts[0].strip())
    T = parse_datatype(parts[1].strip())
    return TypeEquation.TypeEquation(S, T)

# Parses a string representation of a data type 
def parse_datatype(datatype_str):

    # If the string represents the Nat type, return a Nat object
    if (datatype_str == "Nat"):
        return DataType.Nat()
    
    # If the string represents the Bool type, return a Bool object
    elif (datatype_str == "Bool"):
        return DataType.Bool()
    
    # If the string contains the arrow symbol (→), it represents a function 
    # type
    elif("→" in datatype_str):
        parts = datatype_str.split('→')

        # Parses the subtypes of the function type recursively
        for i in range(0, len(parts)):
            parts[i] = parse_datatype(parts[i].replace(' ', ''))
        
        # Divides the parsed subtypes into groups of two
        n = 2
        output = [parts[i:i + n] for i in range(0, len(parts), n)]
        
        # Determine the structure of the function type based on the number of groups
        if(len(output) == 1 and len(output[0]) == 2):
            
            # If there is a single group with two subtypes, creates a FuncType object
            s = output[0][0]
            t = output[0][1]

        if(len(output) > 1 and len(output[1]) == 2):

            # If there are multiple groups and the second group has two 
            # subtypes,create nested FuncType objects for both groups
            s = DataType.FuncType(output[0][0], output[0][1])
            t = DataType.FuncType(output[1][0], output[1][1])

        if(len(output) > 1 and len(output[1]) == 1):

            # If there are multiple groups and the second group has a single subtype,
            # create a nested FuncType object for the first group and 
            # use the single subtype as the second group
            s = DataType.FuncType(output[0][0], output[0][1])
            t = output[1][0]

        # Create a FuncType object representing the parsed function type
        return DataType.FuncType(s, t)

    else:
        # If the string represents a variable type, return a Var object with 
        # the variable name
        return DataType.Var(datatype_str)
