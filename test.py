from numpy import *
from utils import *
from gauss import *
from seidel import *
from iteration import iteration

n = 2 
a = wellConditioned(n)
b = freeTerm(n)
print "Gauss"
print gauss(a, b)
print "Seidel, coeff = 1"
print seidel(a, b, 1e-10)
print "Correct"
print linalg.solve(a, b)
