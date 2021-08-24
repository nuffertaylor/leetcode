def verifyRow(r):
  numW, numB, consec = 0,0,0
  color = True
  for c in r:
    if(c == 'W'): 
      numW+=1
      if color == False:
        color = True
        consec = 0
      consec += 1
    else: 
      numB+=1
      if color == True:
        color = False
        consec = 0
      consec += 1
    if consec == 3: return False
  if numW != numB: return False
  return True

def verifyCols(board):
  for y in range(len(board)):
    numW, numB, consec = 0,0,0
    color = True
    for x in range(len(board)):
      if(board[y][x] == 'W'):
        numW+=1
        if color == False:
          color = True
          consec = 0
        consec+=1
      else:
        numB+=1
        if color == True:
          color = False
          consec = 0
        consec += 1
      if consec == 3: return False
    if numW != numB: return False
  return True

def runProgram():
  n = int(input())
  board = []
  for i in range(n):
    row = input()
    if(not verifyRow(row)):
      return 0
    board.append(row)
  if verifyCols(board):
    return 1
  else:
    return 0

print(runProgram())