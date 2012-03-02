from numpy import *
from utils import *
from gauss import *

n = 10 
a = wellConditioned(n)
b = freeTerm(n)
print a
print b
print gauss(a, b)
print linalg.solve(a, b)
