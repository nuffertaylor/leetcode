s = input()
numE = 0
for c in s:
  if(c=='e'): numE+=1
strBuilder = "h"
for i in range(numE):
  strBuilder += "ee"
print(strBuilder + "y")