from copy import deepcopy
from numpy import matrix, shape, inf 
from utils import *
from numpy.linalg import norm

def simpleIter(a, b, eps = 1e-10, limit = 1000):
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
    if iters >= limit:
      print "Simple iterations method has not succeeded."
      return None
    xOld = x
    x = a * x - b
  print "Iterations in simple iterations method:", iters
  return x
