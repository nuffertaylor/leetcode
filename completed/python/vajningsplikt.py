def doIYield():
  l = [x for x in input().split()]
  #check first - am i attempting to go straight through?
  straight = False
  if(l[0] == "North" and l[1] == "South"):
    straight = True
  elif(l[0] == "South" and l[1] == "North"):
    straight = True
  elif(l[0] == "East" and l[1] == "West"):
    straight = True
  elif(l[0] == "West" and l[1] == "East"):
    straight = True

  if straight:
    ret = "No"
    if(l[0] == "South" and l[2] == "East"):
      ret = "Yes"
    elif(l[0] == "East" and l[2] == "North"):
      ret = "Yes"
    elif(l[0] == "North" and l[2] == "West"):
      ret = "Yes"
    elif(l[0] == "West" and l[2] == "South"):
      ret = "Yes"
    return ret

  #check second - am i attempting to turn left?
  left = False
  if(l[0] == "North" and l[1] == "East"):
    left = True
  elif(l[0] == "East" and l[1] == "South"):
    left = True
  elif(l[0] == "South" and l[1] == "West"):
    left = True
  elif(l[0] == "West" and l[1] == "North"):
    left = True

  if left:
    ret = "No"
    if(l[0]=="South"):
      if(l[2]=="East" or l[2]=="North"):
        ret="Yes"
    elif(l[0]=="East"):
      if(l[2]=="North" or l[2]=="West"):
        ret="Yes"
    elif(l[0]=="North"):
      if(l[2]=="West" or l[2]=="South"):
        ret="Yes"
    elif(l[0]=="West"):
      if(l[2]=="South" or l[2]=="East"):
        ret="Yes"
    return ret
  else:
    return "No"

print(doIYield())