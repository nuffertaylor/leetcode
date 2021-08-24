n = input()
l = [int(x) for x in input().split()]
numTowers=1
for i in range(len(l)):
  if i==0: continue
  if l[i-1] < l[i]:
    numTowers += 1
print(numTowers)