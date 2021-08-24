import sys
res = []
for line in sys.stdin:
  l = line.split()
  x = int(l[0])
  y = int(l[1])
  if x > y:
    res.append(x-y)
  elif y > x:
    res.append(y-x)
  else:
    res.append(0)

for r in res:
  print(r)
