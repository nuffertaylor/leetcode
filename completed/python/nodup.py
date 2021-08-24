usedSoFar = set()
duplicates = False
for s in input().split():
  if s in usedSoFar:
    duplicates = True
  else:
    usedSoFar.add(s)
print("no" if duplicates else "yes")