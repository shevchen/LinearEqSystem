from copy import copy, deepcopy
from numpy import matrix, shape, inf, zeros, nonzero
from utils import *
from numpy.linalg import norm

def simpleIter(a, b, eps = 1e-10):
	a = deepcopy(a)
	b = deepcopy(b)
	#appr = deepcopy(appr)
	if not checkSize(a, b):
		raise Exception("Invalid operands")
	#if not checkSize(a, appr):
	#	raise Exception("Invalid operands, wrong size of approximation")
	if eps == 0:
		raise Exception("Invalid operands, eps should be not != 0")
	n = shape(a)[0]
	a += identityMatrix(n)
	appr_old = matrix([[inf]] * n)
	appr = zeroTerm(n)
	while norm(appr_old - appr) > eps:
                print appr
		appr_old = appr
		appr = a * appr - b
	return appr
