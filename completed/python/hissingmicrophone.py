s = input()
found = False
res = "no hiss"
for c in s:
  if c=='s':
    if found:
      res="hiss"
      break
    else:
      found = True
  else:
    found = False
print(res)