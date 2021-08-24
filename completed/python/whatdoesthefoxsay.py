n = int(input())
numResponses = 0
while numResponses < n:
  noises = [x for x in input().split()]
  l = [x for x in input().split()]
  while " ".join(l) != "what does the fox say?":
    if l[2] in noises:
      noises = [x for x in noises if x != l[2]]
    l = [x for x in input().split()]
  numResponses += 1
  print(" ".join(noises))