from numpy import matrix

def wellConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    for j in range(0, n):
      if i != j:
        m[i, j] = 1. / (j - i) ** 2
      else:
        m[i, j] = 2 * (i + 1)
  return m

def illConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    for j in range(0, n):
      m[i, j] = 1. / (i + j + 1)
  return m

m = wellConditioned(5)
print m
