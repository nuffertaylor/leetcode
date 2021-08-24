l = [int(x) for x in input().split()]
if(l[0] < l[1]):
  diff = str(l[1]-l[0])
  pieces = " piece" if diff == '1' else " pieces"
  print("Dr. Chaz will have " + diff + pieces + " of chicken left over!")
else:
  diff = str(l[0]-l[1])
  pieces = " more piece" if diff == '1' else " more pieces"
  print("Dr. Chaz needs " + diff + pieces + " of chicken!")