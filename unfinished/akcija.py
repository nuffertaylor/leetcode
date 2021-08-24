#passes 2/12 test cases. kattis is stupid and i don't understand what's wrong

n = int(input())
cheapest = []
for i in range(n):
  cheapest.append(int(input()))
cheapest.sort()
for i in range(n//3):
  cheapest.pop(0)
cost = sum(cheapest)

print(cost)