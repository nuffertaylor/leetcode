l=input()
ws,lo,ca,sy=0,0,0,0
for x in l:
  if x=='_': ws+=1
  elif x.islower(): lo+=1
  elif x.isupper(): ca+=1
  else: sy+=1
print(ws/len(l))
print(lo/len(l))
print(ca/len(l))
print(sy/len(l))