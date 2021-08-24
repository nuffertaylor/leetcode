def runProgram():
  l = [int(x) for x in input().split()]

  numRequired = (4 * (l[0] * (l[0] - 1)) // 2) + 1
  numRemaining = numRequired - l[2]*2 - l[1]

  B=0
  A=0
  if(numRemaining < 0): #we have more than enough blocks
    if(l[1] < 1):
      A = 1
  else:
    B = numRemaining//2
    A = numRemaining%2

  print(str(A) + " " + str(B))

runProgram()