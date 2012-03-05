from numpy import matrix, shape

def wellConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(n):
    for j in range(n):
      m[i, j] = (-0.5) ** abs(j - i) / n
    m[i, i] = -1
  return m

def illConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(n):
    for j in range(n):
      m[i, j] = 1. / (i + j + 1)
  return m

def identityMatrix(n):
  m = matrix([[0.] * n] * n)
  for i in range(n):
    m[i, i] = 1
  return m

def freeTerm(n):
  return matrix([[1. * i] for i in range(n)])

def checkSize(a, b):
  aShape = shape(a)
  if len(aShape) != 2 or aShape[0] != aShape[1]:
    return False
  bShape = shape(b)
  if len(bShape) != 2 or bShape[1] != 1:
    return False
  return aShape[0] == bShape[0]

def zeroTerm(n):
  return matrix([[0.]] * n)
