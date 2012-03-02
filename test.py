from numpy import *
from utils import *
from gauss import *

n = 10
a = wellConditioned(n)
b = freeTerm(n)
print gauss(a, b)
print a * transpose(matrix(b))
