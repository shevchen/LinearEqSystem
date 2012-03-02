from numpy import shape

def check(a, b):
  aShape = shape(a)
  if len(aShape) != 2 or aShape[0] != aShape[1]:
    return False
  return len(b) == aShape[0]
