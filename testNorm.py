from utils import *
from numpy.linalg import *

for n in range(50):
  a = illConditioned(n + 1) + identityMatrix(n + 1)
  if norm(a) > 1:
    print "||A + E|| > 1:", (n + 1)
    print a
    exit(1)
print "ok"
