l = [int(x) for x in input().split()]
for i in range(l[2]):
  cards = [int(x) for x in input().split()]
  cards = cards[1:]
  found = False
  for c in cards:
    if c == l[1]:
      found = True
  print("KEEP" if found else "REMOVE")