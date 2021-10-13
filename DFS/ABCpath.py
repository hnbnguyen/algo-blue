# finding the longest path alphabetically in a grid
# searching consecutively starting at grid "A" all the way til the search stops
# DFS, keeping track of a path length array(storing length)
# current complexity
import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0
result = 0
case = 1

while True:
    height, width = map(int, input().split())
    visited = [[False for a in range(width)] for b in range(height)]
    if height == 0 and width == 0:
        break
    grid = []
    for i in range(height):
        grid.append(input())

    start_list = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "A":
                start_list.append([i, j])

    def dfs(at):
        global ans
        x, y = at[0], at[1]
        ans += 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx in range(width) and ny in range(height) and grid[nx][ny] == alpha[ans] and visited[nx][ny] is False:
                dfs([nx, ny])
        # visited[x][y] = False

    for i in range(len(start_list)):
        start = start_list.pop()
        dfs(start)
        result = max(ans, result)
        ans = 0

    print('Case {}: {}'.format(case, result))

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))