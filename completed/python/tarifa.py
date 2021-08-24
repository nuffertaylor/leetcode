cap = int(input())
n = int(input())
ans = cap
for i in range(n):
  p = int(input())
  ans += (cap - p)
print(ans)