from utils import checkSize
from copy import deepcopy
from numpy import matrix, shape
from numpy.linalg import norm

def seidel(a, b, eps = 0, coeff = 1.):
  if not checkSize(a, b):
    raise Exception("Invalid operands")
  a = deepcopy(a)
  n = shape(a)[0]
  for i in range(n):
    if a[i, i] == 0:
      raise Exception("Powerless method")
    b[i] /= a[i, i]
    a[i] /= a[i, i]
  x = matrix([[0.]] * n)
  while norm(a * x - b) > eps:
    nextX = deepcopy(x)
    for i in range(n):
      nextX[i] -= a[i] * nextX - b[i]
    x += coeff * (nextX - x)
  return x
