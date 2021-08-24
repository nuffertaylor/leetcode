import sys
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for line in sys.stdin:
  l = line.split()
  pigLine = ""
  for w in l:
    if w[0] in vowels:
      pigLine += w + "yay "
    else:
      vowelIndex = None
      for i, x in enumerate(w):
        if x in vowels:
          vowelIndex = i
          break
      pigLine += w[vowelIndex:] + w[:vowelIndex] + "ay "
  print(pigLine)