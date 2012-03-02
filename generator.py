from numpy import matrix

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

def column(n):
  return [i for i in range(n)]
