from copy import deepcopy
from numpy import matrix, shape, inf 
from utils import *
from numpy.linalg import norm

def simpleIter(a, b, eps = 1e-10):
  a = deepcopy(a)
  b = deepcopy(b)
  if not checkSize(a, b):
    raise Exception("Invalid operands")
  n = shape(a)[0]
  a += identityMatrix(n)
  x = zeroTerm(n)
  xOld = matrix([[inf]] * n)
  iters = 0
  while norm(xOld - x) > eps:
    iters += 1
    xOld = x
    x = a * x - b
  print "Iterations in simple iterations method:", iters
  return x
