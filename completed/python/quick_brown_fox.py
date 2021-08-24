n = int(input())
results = []
for i in range(n):
  s = input()
  letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  for c in s:
    if c.lower() in letters:
      letters.remove(c.lower())
  if len(letters) > 0:
    results.append("missing " + "".join(letters))
  else:
    results.append("pangram")

for r in results:
  print(r)