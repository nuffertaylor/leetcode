n = int(input())
xmap = {}
ymap = {}
coords = []
for i in range(n):
  l = [int(x) for x in input().split()]
  coords.append([l[0],l[1]])
  if l[0] not in xmap:
    xmap[l[0]] = 0
  if l[1] not in ymap:
    ymap[l[1]] = 0
  xmap[l[0]] += 1
  ymap[l[1]] += 1

total = 0
for i in range(n):
  x = coords[i][0]
  y = coords[i][1]
  total += (xmap[x] - 1) * (ymap[y] - 1)

print(total)
