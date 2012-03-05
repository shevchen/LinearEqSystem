from numpy import *
from numpy.linalg import norm
from utils import *
from gauss import *
from seidel import *
from simpleIter import *

n = 10 
a = illConditioned(n)
b = freeTerm(n)
print "Norm of the matrix + E:", norm(a + identityMatrix(n))
print "Condition number of the matrix", norm(a) * norm(a.getI())
print "Gauss"
print gauss(a, b)
print "Seidel, coeff = 1"
print seidel(a, b)
print "Simple iterations method"
#print simpleIter(a, b)
print "Correct"
print linalg.solve(a, b)
