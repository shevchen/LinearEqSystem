from copy import copy, deepcopy
from numpy import matrix, shape, inf, zeros, nonzero
from utils import checkSize
from numpy.linalg import norm

def idMatrix(n):
	a = zeros((n,n))
	for i in range(n):
		a[i][i] = 1;
	return matrix(a)

def iteration(a, b, appr, eps = 0):
	a = deepcopy(a)
	b = deepcopy(b)
	appr = deepcopy(appr)
	if not checkSize(a, b):
		raise Exception("Invalid operands")
	if not checkSize(a, appr):
		raise Exception("Invalid operands")
	if eps == 0:
		eps = abs(a[a.nonzero()]).min()/100
	n = shape(a)[0]
	a += idMatrix(n)
	appr_old = matrix([[inf]] * n)
	while norm(appr_old - appr) > eps:
		appr_old = appr
		appr = a * appr - b
	return appr
