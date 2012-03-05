from numpy import *
from numpy.linalg import norm
from utils import *
from gauss import *
from seidel import *
from simpleIter import *
from gradient import *

n = 10
a = wellConditioned(n)
b = freeTerm(n)
print "Norm of the matrix + E:", norm(a + identityMatrix(n))
print "Condition number of the matrix:", norm(a) * norm(a.getI())
print "Gauss"
print gauss(a, b)[1]
for i in range(9):
  coeff = 0.2 * (i + 1)
  print "Seidel, coeff =", coeff
  print seidel(a, b, coeff)
print "Simple iterations method"
print simpleIter(a, b)
print "Gradients method"
print grad(a, b)
print "Correct"
print linalg.solve(a, b)
