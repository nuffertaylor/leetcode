w = int(input())
n = int(input())
area = 0
for i in range(n):
  l = [int(x) for x in input().split()]
  area += l[0] * l[1]
print(area//w)