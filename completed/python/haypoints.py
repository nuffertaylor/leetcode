m, n = [int(x) for x in input().split()]
wordMap = {}
for i in range(m):
  l = input().split()
  wordMap[l[0]] = int(l[1])
for i in range(n):
  num = 0
  d = input()
  while d!='.':
    for word in d.split():
      if (word in wordMap):
        num += wordMap[word]
    d = input()
  print(num)