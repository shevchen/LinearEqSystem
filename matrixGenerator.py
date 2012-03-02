from numpy import matrix
from random import random, choice 

def wellConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    absSum = 0
    for j in range(0, n):
      if i != j:
        m[i, j] = random()
        absSum += abs(m[i, j])
    m[i, i] = 2 * absSum * choice([-1, 1])
  return m

def illConditioned(n):
  m = matrix([[0.] * n] * n)
  for i in range(0, n):
    for j in range(0, n):
      m[i, j] = 1. / (i + j + 1)
  return m

m = wellConditioned(5)
print m
