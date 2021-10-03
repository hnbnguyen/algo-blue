import sys
import time
from collections import deque
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


def solve(row,col):
    maze = []
    for i in range(row):
        maze.append(list(input()))
    # Checking number of opening validity
    num_opening = 0
    gate = []
    for i in range(row):
        if col > 1:
            if i == 0 or i == row - 1:
                for j in range(col):
                    if maze[i][j] == ".":
                        num_opening += 1
                        gate.append([i, j])
            else:
                if maze[i][0] == ".":
                    num_opening += 1
                    gate.append([i, 0])
                if maze[i][-1] == ".":
                    num_opening += 1
                    gate.append([i, col-1])
        else:
            if maze[i][0] == ".":
                num_opening += 1
                gate.append([i, 0])
    if num_opening != 2:
        print("invalid")
        return
    # helper function
    def is_road(x, y):
        return maze[x][y] == '.'
    def in_range(x, y):
        return 0 <= x < row and 0 <= y < col

    visited = [[False for i in range(col)] for j in range(row)]
    q = deque()
    q.append(gate[0])
    while len(q) > 0:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        location = q.popleft()
        for i in range(4):
            nx, ny = location[0] + dx[i], location[1] + dy[i]
            if in_range(nx, ny) and is_road(nx, ny) and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])
                if nx == gate[1][0] and ny == gate[1][1]:
                    print("valid")
                    return
    print('invalid')

t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    solve(m,n)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))