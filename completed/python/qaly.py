n = int(input())
accumlated = 0
for i in range(n):
  l = [float(x) for x in input().split()]
  accumlated += (l[0] * l[1])
print(accumlated)
