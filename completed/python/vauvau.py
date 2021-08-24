def calcAggressiveDog(ag, pa, v):
  curState = 0
  agg = True
  while(curState < v):
    if(agg): curState += ag
    else: curState += pa
    agg = not agg
  
  if(agg): return 0
  return 1

def runProgram():
  dogs = [int(x) for x in input().split()]
  visits = [int(x) for x in input().split()]
  for v in visits:
    numAggressiveDogs = calcAggressiveDog(dogs[0], dogs[1], v) + calcAggressiveDog(dogs[2], dogs[3], v)
    if(numAggressiveDogs==2): print("both")
    elif(numAggressiveDogs==1): print("one")
    else: print("none")
    

runProgram()