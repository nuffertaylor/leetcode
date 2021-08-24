import copy

def loopWaterFlow(g, my, mx):
  graph = copy.deepcopy(g)
  for y, row in enumerate(graph):
    for x, c in enumerate(row):
      if(c=='.' or c=='#'): continue
      elif(c=='V'):
        if(y!=my-1):#if we're on the bottom row, skip
          if(graph[y+1][x] == '.'):
            graph[y+1][x] = 'V'
          elif(graph[y+1][x] == '#'):
            if(x!=0) and (graph[y][x-1] != '#'):
              graph[y][x-1] = 'V'
            if(x!=mx-1) and (graph[y][x+1] != '#'):
              graph[y][x+1] = 'V'
      else: print(c + ' is invalid input')
  return graph

def graphToStr(graph):
  stringbuilder = ""
  for row in graph:
    for c in row:
      stringbuilder += c
    stringbuilder += "\n"
  return stringbuilder



def runProgram():
  l = [int(x) for x in input().split()]
  graph = []
  for i in range(l[0]):
    graph.append(list(input()))
  
  while(True):
    updatedG = loopWaterFlow(graph, l[0], l[1])
    if(updatedG==graph):
      break
    else:
      graph = updatedG
  
  print(graphToStr(updatedG))

runProgram()