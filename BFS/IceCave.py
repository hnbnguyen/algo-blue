import sys
import time
from collections import deque
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
# 3 states: . -> # -> _
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(sx, sy, ex, ey):
    q.append([sx, sy])
    game[sx][sy] = 'X'

    while len(q) > 0:
        location = q.popleft()
        x, y = location[0], location[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == ex and ny == ey and game[nx][ny] == 'X':
                print("YES")
                return

            if nx in range(r) and ny in range(c) and game[nx][ny]== '.':
                game[nx][ny] = 'X'
                q.append([nx, ny])
    print("NO")

r, c = map(int, input().split())
game = []
for i in range(r):
    game.append(list(input()))
sx, sy = map(int,input().split())
ex, ey = map(int, input().split())
BFS(sx-1, sy-1, ex -1, ey-1)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))