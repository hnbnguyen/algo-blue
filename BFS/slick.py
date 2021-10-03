from collections import deque

def solve(row, col):
  matrix = []
  slick = 0
  for i in range(row):
    str = input()
    rw = []
    for c in str:
      if (c == '.'):
        rw.append(1)
      else:
        rw.append(0)
    matrix.append(rw)
    # matrix.append(list(map(int, input().split())))
  # print(matrix)
  
  visited = [[False for i in range(col)] for j in range(row)]
  
  def is_oil(x, y):
    return matrix[x][y] == 1
  
  def in_range(x, y):
    return x < row and y < col and x >= 0 and y >= 0
  # finding the first 1 to start searching spill
  for i in range(row):
    for j in range(col):
      # if this is a non-visited slick, then let's visit it (with BFS)
      if matrix[i][j] == 1 and visited[i][j] == False:
        # found a new component, let's start visiting this
        slick += 1
        q = deque()
        visited[i][j] = True
        q.append([i, j])
        
        while len(q)>0:
          location = q.popleft()
          dx = [1, -1, 0, 0]
          dy = [0, 0, -1, 1]
          for a in range(4):
            nx = location[0] + dx[a]
            ny = location[1] + dy[a]
            
            if in_range(nx, ny) and is_oil(nx, ny) and visited[nx][ny] == False:
              visited[nx][ny] = True
              q.append([nx, ny])
  print(slick)       

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  solve(n, m)
  break