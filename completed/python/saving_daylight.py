import sys
for line in sys.stdin:
  l = line.split()
  x = l[3].split(':')
  minutesX = (int(x[0]) * 60) + int(x[1])
  y = l[4].split(':')
  minutesY = (int(y[0]) * 60) + int(y[1])
  minutesPassed = minutesY - minutesX
  
  res = l[0] + " " + l[1] + " " + l[2] + " "
  res += str(minutesPassed//60) + " hours "
  res += str(minutesPassed%60) + " minutes"
  print(res)
