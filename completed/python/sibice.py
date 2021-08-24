import math
def squared(x):
  return x*x
l = [int(x) for x in input().split()]
maxL = math.sqrt(squared(l[1]) + squared(l[2]))
results = []
for i in range(l[0]):
  if(int(input()) <= maxL):
    results.append("DA")
  else:
    results.append("NE")
for r in results:
  print(r)
  