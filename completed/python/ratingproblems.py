l = [int(x) for x in input().split()]
total = 0
for i in range(l[1]):
  total += int(input())
d = 3*(l[0]-l[1])
badR= (total - d)/l[0]
goodR = (total + d)/l[0]
print(str(badR) + " " + str(goodR))