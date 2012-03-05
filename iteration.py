from copy import copy, deepcopy
from numpy import matrix, shape, inf, zeros, nonzero
from utils import *
from numpy.linalg import norm

def iteration(a, b, appr, eps = 0):
	a = deepcopy(a)
	b = deepcopy(b)
	appr = deepcopy(appr)
	if not checkSize(a, b):
		raise Exception("Invalid operands")
	if not checkSize(a, appr):
		raise Exception("Invalid operands, wrong size of approximation")
	if eps == 0:
		raise Exception("Invalid operands, eps should be not != 0")
	n = shape(a)[0]
	a += identityMatrix(n)
	appr_old = matrix([[inf]] * n)
	while norm(appr_old - appr) > eps:
		appr_old = appr
		appr = a * appr - b
	return appr
