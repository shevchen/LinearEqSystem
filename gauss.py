from copy import copy, deepcopy
from numpy import matrix, shape, inf
from utils import checkSize

def gauss(a, b, eps = 0):
  a = deepcopy(a)
  b = deepcopy(b)
  if not checkSize(a, b):
    raise Exception("Invalid operands")
  n = shape(a)[0]
  for i in range(n):
    for j in range(i, n):
      if abs(a[i, j]) > eps:
        a[i], a[j] = copy(a[j]), copy(a[i])
        b[i], b[j] = copy(b[j]), copy(b[i])
        b[i] /= a[i, i]
        a[i] /= a[i, i]
        for k in range(n):
          if k != i:
            b[k] -= a[k, i] * b[i]
            a[k] -= a[k, i] * a[i]
        break
  for i in range(n):
    if abs(a[i, i]) <= eps and abs(b[i, 0]) > eps:
      return 0, None
  for i in range(n):
    if abs(a[i, i]) <= eps:
      return inf, None
  return 1, matrix([[b[i, 0] / a[i, i]] for i in range(n)])
