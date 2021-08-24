def canTakeKnight(b, r, c):
  if (r > 1 and c > 0):
    if b[r-2][c-1] == 'k': return True
  if (r > 1 and c < 4):
    if b[r-2][c+1] == 'k': return True
  if (r > 0 and c > 1):
    if b[r-1][c-2] == 'k': return True
  if (r < 4 and c > 1):
    if b[r+1][c-2] == 'k': return True
  if (r < 3 and c > 0):
    if b[r+2][c-1] == 'k': return True
  if (r < 3 and c < 4):
    if b[r+2][c+1] == 'k': return True
  if (r > 0 and c < 3):
    if b[r-1][c+2] == 'k': return True
  if (r < 4 and c < 3):
    if b[r+1][c+2] == 'k': return True
  return False

def runProgram():
  board = []
  knightCount = 0
  for i in range(5):
    board.append(input())
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == 'k':
        knightCount+=1
        if canTakeKnight(board, row, col):
          return "invalid"
  if knightCount == 9 : return "valid"
  else: return "invalid"

print(runProgram())