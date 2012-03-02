from numpy import *
from utils import *
from gauss import *

n = 5 
a = wellConditioned(n)
b = freeTerm(n)
print a
print b
print gauss(a, b)
print a * transpose(matrix(b))
