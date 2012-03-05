from copy import copy, deepcopy
from numpy import matrix, shape, inf
from utils import checkSize
from numpy.linalg import norm

def grad(a, b, x,eps = 0):
    a = matrix(deepcopy(a))
    b = matrix(deepcopy(b))
    x = matrix(x)
    if not checkSize(a, b):
        raise Exception("Invalid operands.")
    n = shape(a)[0]
    r1 = b - a * x
    r2 = b - a.transpose() * x
    p1 = r1
    p2 = r2
    x0 = matrix([[inf]] * n)
    while norm(r1) > eps:
        koef = (r2.transpose() * r1).item(0) / (p2.transpose() * (a * p1)).item(0)
        x0 = x
        x = x0 + koef * p1
        r1_new = r1 - koef * a * p1
        r2_new = r2 - koef * a.transpose() * p2
        beta = (r2_new.transpose() * r1_new).item(0) / (r2.transpose() * r1).item(0)
        r1 = r1_new
        r2 = r2_new
        p1 = r1 + beta * p1
        p2 = r2 + beta * p2
    return x
