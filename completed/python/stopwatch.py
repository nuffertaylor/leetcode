n = int(input())
#first check that the stopwatch is stopped
if n % 2 == 0:
  t = []
  for i in range(n):
    t.append(int(input()))
  
  res = 0
  for i in range(0, n, 2):
    res += (t[i+1] - t[i])
  
  print(res)

#odd number of presses = still running
else:
  print("still running")
