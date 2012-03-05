from utils import *
from numpy.linalg import *

def checkNorm(matrixGen, n):
	fl = True
	for i in range(50):
		a = matrixGen(i + 1) + identityMatrix(i + 1)
		if norm(a) > 1:
			fl = False
			print "||A + E|| > 1:", (n + 1)
			print a
			break
	if fl:
		print "ok"
	return

print "ill conditioned:"
checkNorm(illConditioned, 50)
print "well conditioned:"
checkNorm(wellConditioned, 50)
