def rotate(w):
  val = 0
  for c in w:
    val += ord(c) - 65
  res = ""
  for c in w:
    n = (ord(c)-65+val)%26
    res += chr(n+65)
  return res

def merge(w,k):
  res = ""
  for i in range(len(w)):
    res += chr((((ord(w[i])-65)+(ord(k[i])-65))%26)+65)
  return res

def runProgram():
  w = input()
  word = rotate(w[:len(w)//2])
  key = rotate(w[len(w)//2:])
  print(merge(word,key))

runProgram()


