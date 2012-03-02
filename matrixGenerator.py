from numpy import matrix

def wellConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    for j in range(0, n):
      m[i, j] = (-0.5) ** abs(j - i) 
  return m

def illConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    for j in range(0, n):
      m[i, j] = 1. / (i + j + 1)
  return m

m = wellConditioned(5)
print m
