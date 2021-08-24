n = int(input())
for x in range(n):
  l = [int(x) for x in input().split()]
  numPow = l[0]-1
  sumOf = sum(l[1:])
  print(sumOf-numPow)