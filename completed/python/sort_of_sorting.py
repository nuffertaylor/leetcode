import heapq
#passes 1/6

def sortNameList(nl):
  pq = []
  for i, n in enumerate(nl):
    heapq.heappush(pq, (int(hex(ord(n[0])), 0), int(hex(ord(n[1])), 0), i, n))
  return pq

nameList = []
results = []
for zed in range(500):
  x = input()
  if x.isnumeric():
    x = int(x)
    if x == 0: 
      results = results[:len(results)-1]
      break
    nameList = []
    for h in range(x):
      nameList.append(input())
    q = sortNameList(nameList)
    for h in range(len(q)): 
      results.append(heapq.heappop(q)[3])
    results.append("")
for r in results:
  print(r)