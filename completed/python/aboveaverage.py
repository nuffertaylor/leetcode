n = int(input())
for i in range(n):
  l = [int(x) for x in input().split()]
  nums = l[1:]
  avg = sum(nums)/len(nums)
  aboveAvg = 0
  for x in nums:
    if avg < x:
      aboveAvg += 1
  res = aboveAvg/len(nums)
  res = res * 100
  print("{:.3f}".format(res) + "%")
