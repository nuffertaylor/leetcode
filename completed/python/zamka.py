def getSumOfDigits(n):
  sod = 0
  for c in str(n):
    sod += int(c)
  return sod

l = int(input())
d = int(input())
x = int(input())

for n in range(l, d+1, 1):
  if getSumOfDigits(n) == x:
    print(n)
    break
for m in range (d, l-1, -1):
  if getSumOfDigits(m) == x:
    print(m)
    break