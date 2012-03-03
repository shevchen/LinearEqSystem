from copy import copy, deepcopy
from numpy import matrix, shape, inf, zeros
from utils import checkSize

def idMatrix(n):
	a = zeros(n,n)
	for i in range(n):
		a[i][i] = 1;
	return a

def iter(a, b, appr):
	a = deepcopy(a)
	b = deepcopy(b)
	if not checkSize(a, b):
		raise Exception("Invalid operands")
	n = shape(a)[0]

	return 0
