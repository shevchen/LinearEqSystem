from numpy import matrix, shape

def wellConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(n):
    for j in range(n):
      m[i, j] = (-0.5) ** abs(j - i) 
  return m

def illConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(n):
    for j in range(n):
      m[i, j] = 1. / (i + j + 1)
  return m

def freeTerm(n):
  return [i for i in range(n)]

def checkSize(a, b):
  aShape = shape(a)
  if len(aShape) != 2 or aShape[0] != aShape[1]:
    return False
  return aShape[0] == len(b)
