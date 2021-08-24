import sys

n, q = [int(x) for x in input().split()]
dbx = [0] * n #value of last 'set'
dby = [-1] * n #index of last 'set' 
curRestart = 0
restartIndex = 0
curIndex = 0
for l in sys.stdin:
  if curIndex==q: break
  splitStr = l.split()

  if splitStr[0] == "RESTART":
    restartIndex = curIndex
    curRestart = int(splitStr[1])

  elif splitStr[0] == "SET":
    dbx[int(splitStr[1])-1] = int(splitStr[2])
    dby[int(splitStr[1])-1] = curIndex

  elif splitStr[0] == "PRINT":
    if(restartIndex > dby[int(splitStr[1])-1]):
      print(curRestart)
    else:
      print(dbx[int(splitStr[1])-1])

  curIndex += 1