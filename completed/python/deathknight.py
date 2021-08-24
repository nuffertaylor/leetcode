n = int(input())
wins = 0
for z in range(n):
  s = input()
  win = True
  for i in range(1, len(s), 1):
    if s[i-1] == 'C' and s[i] == 'D':
      win = False
      break
  if win:
    wins +=1
print(wins)
