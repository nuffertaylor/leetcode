minions = int(input())
preferences = []
minT, maxT = 2147483647, 0
for i in range(minions):
  pref = [int(x) for x in input().split()]
  if pref[0] < minT: minT = pref[0]
  if maxT < pref[1]: maxT = pref[1]
  preferences.append(pref)
rooms = []
for i in range(minT, maxT+1, 1):
  rooms[i] = []

for i, pref in enumerate(preferences):
  for x in range(pref[0],pref[1]+1,1):
    rooms[x].append(i)

remainingM = []
for i in range(minions):
  remainingM[i] = True

maxM = (0, 0) #(numMinions, roomIndex)
for i, m in enumerate(rooms):
  if len(m) > maxM[0]:
    maxM = (len(m), i)
