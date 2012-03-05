from numpy import *
from utils import *
from gauss import *
from seidel import *
from simpleIter import *

n = 10 
a = wellConditioned(n)
b = freeTerm(n)
print "Gauss"
print gauss(a, b)
print "Seidel, coeff = 1"
print seidel(a, b)
print "Simple iterations"
print simpleIter(a, b)
print "Correct"
print linalg.solve(a, b)
