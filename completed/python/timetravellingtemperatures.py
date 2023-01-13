def program(): 
  x, y = [int(x) for x in input().split()]
  #x is the point on scale B where scale A reads "0"
  #y is the number of degrees in B that equal a single degree change in A
  #Output the temperature where both scales are the same.
  #If no such temperature exists, output
  fail = "IMPOSSIBLE"
  #If more than one such point exists, output
  succ = "ALL GOOD"
  tempOfB = x
  changeInB = y

  #we're really trying to find the intersection of two lines
  #the equation for line A is flat. just a simple y = x
  #the equation for line B is y = mx + b, where b is the temp at 0, and m is the change in B
  #so y = (changeInB)x + (tempOfB)

  #so now we do some basic algebra
  #x = (changeInB)x + (tempOfB)
  #(1-changeInB)x = tempOfB
  #x = tempOfB / (1-changeInB)
  #tada
  #if (1 - changeInB) == 0 , impossible

  #they're the same line
  if(tempOfB == 0 and changeInB == 1): return succ
  #ezclap we already know the intersection
  if(tempOfB == 0): return 0

  divisor = 1 - changeInB
  #can't divide by 0, impossible answer
  if(divisor == 0): return fail
  res = tempOfB / divisor
  return res

print(program())