#https://open.kattis.com/problems/knightjump
#passes 5/13 cases
import math
import heapq

#create priorityqueue
def genPQFromBoard(board):
  pq = []
  start = None
  for x, row in enumerate(board):
    for y, c in enumerate(row):
      if(c == 'K'): #identify location of K to set as cost 0
        heapq.heappush(pq, (0, x, y))
      elif(c == '#'): #set '#' as impossible spaces
        heapq.heappush(pq, (math.inf, x, y))
      else: #these spaces can be visited, but because we want to differentiate from #, we'll just initalize them with a large non-inf cost
        heapq.heappush(pq, (2147483647, x, y))
  return pq

def findIndexOfCoords(pq, x, y):
  for i, t in enumerate(pq):
    if int(t[1]) == x and int(t[2]) == y:
      return i
  return None

#pq = priorityqueue
#res = results in 2d array
#m = max boundary for calculating possible knight moves
def moveKnight(pq, res, m):
  #if len==0, we've finished
  if len(pq) == 0:
    return res
  heapq.heapify(pq) #just in case
  #take the item from the top of the priority queue (first run is starting pos)
  curPos = heapq.heappop(pq)
  x = curPos[1]
  y = curPos[2]
  res[x][y] = curPos[0]
  #8 possible knight moves
  if(x+2 < m):
    if(y+1 < m):
      index = findIndexOfCoords(pq, x+2,y+1)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x+2, y+1)
    if(y-1 > -1):
      index = findIndexOfCoords(pq, x+2,y-1)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x+2,y-1)
  if(x-2 > -1):
    if(y+1 < m):
      index = findIndexOfCoords(pq, x-2,y+1)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x-2,y+1)
    if(y-1 > -1):
      index = findIndexOfCoords(pq, x-2,y-1)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x-2,y-1)
  if(y+2 < m):
    if(x+1 < m):
      index = findIndexOfCoords(pq, x+1,y+2)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x+1,y+2)
    if(x-1 > -1):
      index = findIndexOfCoords(pq, x-1,y+2)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x-1,y+2)
  if(y-2 > -1):
    if(x+1 < m):
      index = findIndexOfCoords(pq, x+1,y-2)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x+1,y-2)
    if(x-1 > -1):
      index = findIndexOfCoords(pq, x-1,y-2)
      if index != None:
        if curPos[0]+1 < pq[index][0] and pq[index][0] != math.inf:
          pq[index] = (curPos[0] + 1, x-1,y-2)
  return moveKnight(pq, res, m)

n = int(input())
b = []
for i in range(n):
  b.append(list(input()))

#verify cost to reach (0,0) isn't inf
if b[0][0] == '#':
  print(-1)
  quit()

q = genPQFromBoard(b)
costBoard = [[0 for x in range(n)] for x in range(n)]
res = moveKnight(q, costBoard, n)
if(res[0][0] < 2147483647): #if it's max int value, we never found a solution.
  print(res[0][0])
else:
  print(-1)
