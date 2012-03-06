from copy import deepcopy
from numpy import matrix, shape, inf 
from utils import *
from numpy.linalg import norm
from math import sqrt
from pylab import *

it = []
norms = []

def launchSimpleIter(a, b, eps = 1e-10, limit = 1000):
  x = simpleIter(a, b, eps, limit)
  if x is None:
    print 'The simple iteration method has failed.'
  else:
    print x
    print "Iterations in simple iteration method:", len(it)
  plot(it, norms, 'b', linewidth = 2.0)
  plot(it, [eps] * len(it), 'r', linewidth = 1.0)
  xlabel('Iteration')
  ylabel('||Xi - Xi-1||')
  title('Simple iteration method')
  grid(True)
  show()


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
    xOld = x
    x = a * x - b
    iters += 1
    curNorm = norm(xOld - x)
    if iters >= limit or curNorm > maxNorm:
      return None
    it.append(iters)
    norms.append(curNorm)
  return x
