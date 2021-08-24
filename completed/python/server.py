def runProgram():
  n, t = [int(x) for x in input().split()]
  s, res = 0, 0
  for x in input().split():
    s += int(x)
    if s > t:
      return res
    res += 1
  return res

print(runProgram())