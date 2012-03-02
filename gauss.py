from checker import check

def gauss(a, b, eps = 1e-10):
  if not check(a, b):
    raise Exception("Invalid matrix")
  n = len(b)  
  for i in range(n):
    for j in range(i, n):
      if abs(a[i, j]) > eps:
        a[i], a[j] = a[j], a[i]
        b[i], b[j] = b[j], b[i]
        for k in range(i + 1, n):
          a[i, k] /= a[i, i]
        b[i] /= a[i, i]
        a[i, i] = 1
        for k in range(n):
          if k != i:
            for l in range(i + 1, n):
              a[k, l] -= a[k, i] * a[i, l]
            a[k, i] = 0
        break
  for i in range(n):
    if abs(a[i, i]) < eps and abs(b[i]) > eps:
      return 0, None
  for i in range(n):
    if abs(a[i, i]) < eps:
      return float("infinity"), None
  return 1, [b[i] / a[i, i] for i in range(n)]
