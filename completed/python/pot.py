n = int(input())
sum = 0
for i in range(n):
  s = input()
  sum += int(s[:len(s)-1]) ** int(s[len(s)-1:])
print(sum)