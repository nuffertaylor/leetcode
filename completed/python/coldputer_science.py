n = int(input())
temps = [int(x) for x in input().split()]
res = 0
for t in temps:
  if t < 0:
    res+=1
print(res)