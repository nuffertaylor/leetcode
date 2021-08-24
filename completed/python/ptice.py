def genAdrianSequence(n):
  val = ""
  while len(val) < n:
    val += "ABC"
  return val[:n]

def genBrunoSequence(n):
  val = ""
  while len(val) < n:
    val += "BABC"
  return val[:n]

def genGoranSequence(n):
  val = ""
  while len(val) < n:
    val += "CCAABB"
  return val[:n]

n = int(input())
correct = input()

adrianAns = genAdrianSequence(n)
brunoAns = genBrunoSequence(n)
goranAns = genGoranSequence(n)
aScore, bScore, gScore = 0, 0, 0

for i, c in enumerate(correct):
  if c == adrianAns[i]: aScore +=1
  if c == brunoAns[i]: bScore += 1
  if c == goranAns[i]: gScore += 1

highest = aScore
if bScore > highest: highest = bScore
if gScore > highest: highest = gScore
print(highest)
if aScore == highest: print("Adrian")
if bScore == highest: print("Bruno")
if gScore == highest: print("Goran")
