x,y,n=[int(x) for x in input().split()]
i=1
while i<=n:
  s=""
  if i%x==0: s+="Fizz"
  if i%y==0: s+="Buzz"
  if s=="": s=str(i)
  print(s)
  i+=1