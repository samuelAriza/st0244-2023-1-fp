from constraints import get
from unify import *
import sys

# Gets the constraint set from the input file specified in the command line arguments
constraint = get(sys.argv[1])

# Performs the unification on the constraint set
unify(constraint)
