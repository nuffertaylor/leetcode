bssf = 0
bssfIndex = 0
for i in range(1, 6, 1):
  l = [int(x) for x in input().split()]
  if sum(l) > bssf:
    bssf = sum(l)
    bssfIndex = i
print(str(bssfIndex) + " " + str(bssf))
