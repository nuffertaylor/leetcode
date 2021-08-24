# import heapq

#this works but it's too slow. passes 6
#use dynamic programming?
def calcRhymePower(w1,w2):
  power = 0
  i = j = 0
  while(True):
    if(w1[i] == w2[j]):
      if(i==len(w1)-1 or j ==len(w2)-1):
        power = 0
        break
      else:
        power +=1
    else: break
    i+=1
    j+=1
  return power

def runProgram():
  n = int(input())
  words = []
  # visited = set()
  # wordHeap = []
  for i in range(n):
    words.append(input()[::-1])
  words.sort()

  best = 0
  for i in range(len(words)):
    if i == 0: continue
    else:
      best = max(best, calcRhymePower(words[i-1], words[i]))

  print(best)

runProgram()