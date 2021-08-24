#passes 12/19 test cases

board = [[int(x) for x in input().split()] for i in range(4)]
direction = int(input())

if direction == 0: #left
  for y in range(4):
    for i in range(4):
      for x in range(3,0,-1):
        #move each piece as far to the left as possible(through blanks, no merge yet)
        if(board[y][x-1] == 0):
          board[y][x-1] = board[y][x]
          board[y][x] = 0
    for x in range(3):
      #if two touching pieces share the same number, merge
      if(board[y][x+1] == board[y][x]):
        board[y][x] = board[y][x] * 2
        board[y][x+1] = 0
    #in case any combined, move left with zeros again.
    for i in range(4):
      for x in range(3,0,-1):
        if(board[y][x-1] == 0):
          board[y][x-1] = board[y][x]
          board[y][x] = 0
#the only difference between left and right are +/-, and which way we check
elif direction == 2: #right
  for y in range(4):
    for i in range(4):
      for x in range(3):
        if(board[y][x+1] == 0):
          board[y][x+1] = board[y][x]
          board[y][x] = 0
    for x in range(3,0,-1):
      if(board[y][x-1] == board[y][x]):
        board[y][x] = board[y][x] * 2
        board[y][x-1] = 0
    for i in range(4):
      for x in range(3):
        if(board[y][x+1] == 0):
          board[y][x+1] = board[y][x]
          board[y][x] = 0

elif direction == 1: #up
  for x in range(4):
    for i in range(4):
      for y in range(3,0,-1):
        if(board[y-1][x] == 0):
          board[y-1][x] = board[y][x]
          board[y][x] = 0
    for y in range(3):
      if(board[y][x] == board[y+1][x]):
        board[y][x] = board[y][x] * 2
        board[y+1][x] = 0
    for i in range(4):
      for y in range(3,0,-1):
        if(board[y-1][x] == 0):
          board[y-1][x] = board[y][x]
          board[y][x] = 0
#same goes for up&down
elif direction == 3: #down
  for x in range(4):
    for i in range(4):
      for y in range(3):
        if(board[y+1][x] == 0):
          board[y+1][x] = board[y][x]
          board[y][x] = 0
    for y in range(3,0,-1):
      if(board[y][x] == board[y-1][x]):
        board[y][x] = board[y][x] * 2
        board[y-1][x] = 0
    for i in range(4):
      for y in range(3):
        if(board[y+1][x] == 0):
          board[y+1][x] = board[y][x]
          board[y][x] = 0
else:
  print("invalid direction")

for row in board:
  strBuilder = ""
  for e in row:
    strBuilder = strBuilder + str(e) + " "
  print(strBuilder[:len(strBuilder)-1])