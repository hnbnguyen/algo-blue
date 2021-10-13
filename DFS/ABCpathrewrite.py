import sys
sys.setrecursionlimit(10000000)

DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

case = 0
while True:
    case += 1
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    grid = []
    for i in range(h):
        grid.append(input())
    path = [[0] * w for i in range(h)]

    def find_path(x, y):
        if path[x][y]:
            return path[x][y]
        max_path = 0
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w or ord(grid[nx][ny]) != ord(grid[x][y]) + 1:
                continue
            max_path = max(max_path, find_path(nx, ny))
        path[x][y] = max_path + 1
        return path[x][y]

    res = 0
    for x in range(h):
        for y in range(w):
            if grid[x][y] == 'A':
                res = max(res, find_path(x, y))
    print('Case {}: {}'.format(case, res))
