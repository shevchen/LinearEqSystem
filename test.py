from numpy import *
from numpy.linalg import norm
from utils import *
from gauss import *
from seidel import *
from simpleIter import *
from gradient import *

n = 10
a = illConditioned(n)
b = freeTerm(n)
launchSeidel(a, b)
#launchSimpleIter(a, b)
#launchGradient(a, b)
#print gauss(a, b)[1]
#print "Norm of the matrix + E:", norm(a + identityMatrix(n))
#print "Condition number of the matrix:", norm(a) * norm(a.getI())
#for i in range(9):
#  coeff = 0.2 * (i + 1)
#  print "Seidel, coeff =", coeff
#  print seidel(a, b, coeff)
#print "Correct"
#print linalg.solve(a, b)
