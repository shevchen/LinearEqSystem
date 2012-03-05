from utils import *
from numpy.linalg import *

def checkNorm(matrixGen, n):
  for i in range(n):
    a = matrixGen(i + 1) + identityMatrix(i + 1)
    if norm(a) > 1:
      print "||A + E|| > 1:", (i + 1)
      print a
      return	
  print "ok"

print "ill conditioned:"
checkNorm(illConditioned, 50)
print "well conditioned:"
checkNorm(wellConditioned, 50)
