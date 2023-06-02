import DataType 
import TypeEquation
from unify import *

f = TypeEquation.TypeEquation(DataType.Var("X"), DataType.Nat())
s = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Var("X"), DataType.Var("X")))
n = TypeEquation.TypeEquation(DataType.Var("Y"), DataType.FuncType(DataType.Nat(), DataType.Var("Y")))
pp = TypeEquation.TypeEquation(DataType.FuncType(DataType.Var("X"), DataType.Var("Y")), DataType.FuncType(DataType.Nat(), DataType.Bool()))
mm = TypeEquation.TypeEquation(DataType.FuncType(DataType.Var("Y"), DataType.Var("X")), DataType.FuncType(DataType.Bool(), DataType.Nat()))


constraints = [f, s]
unify(constraints)

