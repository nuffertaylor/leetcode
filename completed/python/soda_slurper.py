l = [int(x) for x in input().split()]
e = l[0]
f = l[1]
c = l[2]

sodaDrunk = ((e+f)//c)
# get the remainder of cashing in all bottles so far + new bottles
bottlesRemaining = ((e + f) % c) + sodaDrunk

while (bottlesRemaining >= c):
  sodaDrunk += (bottlesRemaining//c)
  bottlesRemaining = (bottlesRemaining % c) + (bottlesRemaining//c)
print(sodaDrunk)
