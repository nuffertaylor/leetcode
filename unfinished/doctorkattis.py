import sys
import heapq

def calcInfection(x):
  return 100-x

n = int(input())
commandNum = 0
pq = []
for line in sys.stdin:
  r = line.split()
  if r[0] == "0":
    heapq.heappush(pq, (calcInfection(int(r[2])), commandNum, r[1]))
  elif r[0] == "1":
    toRemove, toAdd = None, None
    for c in pq:
      if r[1] == c[2]:
        toRemove = c
        toAdd = (calcInfection(c[0] + int(r[2])), c[1], c[2])
        break
    pq.remove(toRemove)
    pq.append(toAdd)
    heapq.heapify(pq)
  elif r[0] == "2":
    #check if it's the top cat
    if r[1] == pq[0][2]:
      heapq.heappop(pq)
    else:
      toRemove = None
      for c in pq:
        if r[1] == c[2]:
          toRemove = c
          break
      pq.remove(toRemove)
      heapq.heapify(pq)
  elif r[0] == "3":
    if(len(pq) > 0):
      print(pq[0][2])
    else:
      print("The clinic is empty")
  commandNum += 1
  if commandNum == n: break