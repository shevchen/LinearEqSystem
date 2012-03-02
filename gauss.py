from copy import deepcopy
from numpy import shape, inf
from utils import checkSize

def gauss(a, b, eps = 0):
  a = deepcopy(a)
  b = deepcopy(b)
  if not checkSize(a, b):
    raise Exception("Invalid operands")
  n = len(b)
  for i in range(n):
    for j in range(i, n):
      if abs(a[i, j]) > eps:
        a[i], a[j] = a[j], a[i]
        b[i], b[j] = b[j], b[i]
        b[i] /= a[i, i]
        a[i] /= a[i, i]
        for k in range(n):
          if k != i:
            b[k] -= a[k, i] * b[i]
            a[k] -= a[k, i] * a[i]
        break
  for i in range(n):
    if abs(a[i, i]) <= eps and abs(b[i]) > eps:
      return 0, None
  for i in range(n):
    if abs(a[i, i]) <= eps:
      return inf, None
  return 1, [b[i] / a[i, i] for i in range(n)]
