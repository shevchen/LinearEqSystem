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
        for k in range(i + 1, n):
          a[i, k] /= a[i, i]
        b[i] /= a[i, i]
        a[i, i] = 1
        for k in range(n):
          if k != i:
            for l in range(i + 1, n):
              a[k, l] -= a[k, i] * a[i, l]
            a[k, i] = 0
        break
  for i in range(n):
    if abs(a[i, i]) <= eps and abs(b[i]) > eps:
      return 0, None
  for i in range(n):
    if abs(a[i, i]) <= eps:
      return inf, None
  return 1, [b[i] / a[i, i] for i in range(n)]
