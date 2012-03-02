from numpy import shape

def check(a, b):
  aShape = shape(a)
  if len(aShape) != 2 or aShape[0] != aShape[1]:
    return False
  bShape = shape(b)
  return len(bShape) == 1 and aShape[0] == bShape[0]
