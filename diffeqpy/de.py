import sys
from . import load_julia_package
sys.modules[__name__] = load_julia_package("DifferentialEquations") # mutate myself
