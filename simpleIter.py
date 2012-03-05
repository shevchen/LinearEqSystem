from copy import deepcopy
from numpy import matrix, shape, inf 
from utils import *
from numpy.linalg import norm
from math import sqrt

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
  maxNorm = 1e100 * n
  while norm(xOld - x) > eps:
    iters += 1
    xOld = x
    x = a * x - b
    if iters >= limit or norm(xOld - x) > maxNorm:
      print "Simple iterations method has not succeeded."
      return None
  print "Iterations in simple iterations method:", iters
  return x
