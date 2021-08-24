def runProgram():
  n = int(input())
  countries = []
  sumPlayers = 0
  sumRef = 0
  for i in range(n):
    l = [int(x) for x in input().split()]
    sumPlayers += l[0]
    sumRef += l[1]
    countries.append(l)

  total = 0
  for c in countries:
    total += c[0] * (sumPlayers - c[0])  * (sumRef - c[1]) #this accounts for all possible combos, excepting the 2nd player and ref could be from the same country
    total -= c[0] * c[1] * (sumPlayers - c[0]) #thus we preemptively delete those occurences on this line as we iterate through
  
  print(total//2)

runProgram()