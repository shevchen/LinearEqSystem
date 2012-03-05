from numpy import *
from numpy.linalg import norm
from utils import *
from gauss import *
from seidel import *
from simpleIter import *

n = 10 
a = illConditioned(n)
#a2 = wellConditioned(n)
b = freeTerm(n)
print "Condition number of ill one", norm(a) * norm(a.getI())
#print "Condition number of good one", norm(a2) * norm(a2.getI())
print "Gauss"
print gauss(a, b)
print "Seidel, coeff = 1"
print seidel(a, b)
print "Simple iterations method"
print iteration(a, b)
print "Correct"
print linalg.solve(a, b)
