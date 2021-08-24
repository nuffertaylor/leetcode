n = int(input())
results = []
for i in range(n):
  s = input()
  if s[:len("Simon says")] == "Simon says":
      results.append(s[len("Simon says "):])
for r in results:
  print(r)