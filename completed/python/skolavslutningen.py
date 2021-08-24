import itertools

def hasConsistentCol(lines, x):
    curRowVal = None
    for y in range(len(lines)):
      if y == 0: curRowVal = lines[y][x]
      elif curRowVal != lines[y][x]:
        return False
    return True

def runProgram():
  n, m, k = [int(x) for x in input().split()]
  # lettersAvail = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # lettersAvail = lettersAvail[:k]
  lines = []
  for i in range(n):
    lines.append(input())

  numColors = k
  sharesColor, uniqueColor = [], set()
  for x in range(m):
    if(hasConsistentCol(lines, x)):
      uniqueColor.add(lines[0][x])
    else:
      sharesList = []
      for y in range(len(lines)):
        sharesList.append(lines[y][x])

      noCommon = True
      for i, s in enumerate(sharesColor):
        if(bool(set(s) & set(sharesList))):
          sharesColor[i] = list(set(s + sharesList))
          noCommon = False
          break
      if noCommon: sharesColor.append(sharesList)

  reallyUnique = []
  for c in uniqueColor:
    if c not in list(itertools.chain.from_iterable(sharesColor)):
      reallyUnique.append(c)
  
  print(len(sharesColor) + len(reallyUnique))

runProgram()