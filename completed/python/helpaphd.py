n = int(input())
for i in range(n):
  h = input()
  if (h=="P=NP"):
    print("skipped")
  else:
    l = [int(x) for x in h.split('+')]
    print(l[0]+l[1])
    