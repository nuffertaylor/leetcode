n = int(input())
costs = []
for i in range(n):
  costs.append(int(input()))

minCost = 2147483647
#use circular array
for x in range(n):
  cost = costs[x] + costs[((x+n-2)%n)]
  if cost < minCost:
    minCost = cost

print(minCost)