from utils import checkSize, zeroTerm
from copy import deepcopy
from numpy import matrix, shape
from numpy.linalg import norm

def seidel(a, b, coeff = 1., eps = 1e-10, limit = 1000):
  if not checkSize(a, b):
    raise Exception("Invalid operands")
  a = deepcopy(a)
  b = deepcopy(b)
  n = shape(a)[0]
  for i in range(n):
    if a[i, i] == 0:
      raise Exception("Powerless method")
    b[i] /= a[i, i]
    a[i] /= a[i, i]
  x = zeroTerm(n)
  iters = 0
  while norm(a * x - b) > eps:
    iters += 1
    if iters >= limit:
      print "Seidel method has not succeeded."
      return None
    nextX = deepcopy(x)
    for i in range(n):
      nextX[i] -= a[i] * nextX - b[i]
    x += coeff * (nextX - x)
  print "Iterations in Seidel method:", iters
  return x
