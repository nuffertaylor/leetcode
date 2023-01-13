n = int(input())
answers = [input() for i in range(n)]
correct = 0
for i in range(n-1):
  if(answers[i] == answers[i+1]):
    correct += 1
print(correct)
