from utils import checkSize, zeroTerm
from copy import deepcopy
from numpy import matrix, shape
from numpy.linalg import norm
from math import sqrt
from pylab import *

it = []
norms = []

def launchSeidel(a, b, coeff = 1., eps = 1e-10, limit = 1000):
  x = seidel(a, b, coeff, eps, limit)
  if x is None:
    print 'The Seidel method has failed.'
  else:
    print x
    print "Iterations in Seidel method:", len(it)
  plot(it, norms, 'b', linewidth = 2.0)
  plot(it, [eps] * len(it), 'r', linewidth = 1.0)
  xlabel('Iteration')
  ylabel('||A x - b||')
  title('Seidel method with coeff = ' + str(coeff))
  grid(True)
  show()

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
  maxNorm = 1e100 * n
  while norm(a * x - b) > eps:
    nextX = deepcopy(x)
    for i in range(n):
      nextX[i] -= a[i] * nextX - b[i]
    x += coeff * (nextX - x)
    iters += 1
    curNorm = norm(a * x - b)
    if iters >= limit or curNorm > maxNorm:
      return None
    it.append(iters)
    norms.append(curNorm)
  return x
