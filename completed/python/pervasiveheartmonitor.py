import sys

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

for line in sys.stdin:
  values = []
  name = ""
  for x in line.split():
    if is_number(x):
      values.append(float(x))
    else:
      name += " " + x 
  
  av = sum(values)/len(values)
  print("{:.6f}".format(av) + name)



