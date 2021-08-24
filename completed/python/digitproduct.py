x = input()
while len(x) > 1:
  a = 1
  for d in x:
    if(d == '0'): continue
    else: a = a * int(d)
  x = str(a)
print(x)