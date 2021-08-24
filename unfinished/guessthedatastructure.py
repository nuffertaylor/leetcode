import copy
import heapq
import sys

#passes 1/2

results = []
for line in sys.stdin:
  n = int(line)
  stack, queue, priorityQueue = True, True, True
  stackList, queueList, pqList = [], [], []
  for i in range(n):
    l = [int(x) for x in input().split()]
    if(l[0] == 1):
      stackList.append(l[1])
      queueList.append(l[1])
      heapq.heappush(pqList, (2147483647 - l[1], l[1]))
    elif(l[0] == 2):
      if(len(stackList) == 0):
        stack = False
        queue = False
        priorityQueue = False
        break
      if(l[1] != stackList.pop()):
        stack = False
      if(l[1] != queueList.pop(0)):
        queue = False
      if(l[1] != heapq.heappop(pqList)[1]):
        priorityQueue = False
  if(stack == True and queue == False and priorityQueue == False):
    results.append("stack")
  elif(stack == False and queue == True and priorityQueue == False):
    results.append("queue")
  elif(stack == False and queue == False and priorityQueue == True):
    results.append("priority queue")
  elif(stack == False and queue == False and priorityQueue == False):
    results.append("impossible")
  else:
    results.append("not sure")

for r in results:
  print(r)