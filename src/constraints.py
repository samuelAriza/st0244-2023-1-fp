from parse import parse_type_equation, parse_datatype

def get(filename):
    c = []
    with open (filename) as archivo:
        for linea in archivo:
            c.append(parse_type_equation(linea.replace(' ', '').replace('\n', '')))
    return c



