n = int(input())
for i in range(n):
  l = [int(x) for x in input().split()]
  if(l[1] - l[2] < l[0]):
    print("do not advertise")
  elif(l[1] - l[2] > l[0]):
    print("advertise")
  else:
    print("does not matter")
