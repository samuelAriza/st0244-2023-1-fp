from constraints import get
from unify import *
import sys

constraint = get(sys.argv[1])
unify(constraint)


