a, b, c = True, False, False
strIn = input()
for s in strIn:
  if s == 'A':
    temp = a
    a = b
    b = temp
  elif s == 'B':
    temp = b
    b = c
    c = temp
  elif s == 'C':
    temp = c
    c = a
    a = temp
if a == True:
  print(1)
elif b == True:
  print(2)
elif c == True:
  print(3)