import sys
import time
from collections import deque
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sheep_count = wolf_count = 0
# instead of using visited, change the visited block into fence
def BFS(a, b):
    print('visit', a, b)
    global sheep_count, wolf_count
    q = deque()
    q.append([a, b])

    # check if a and b happens to be sheep or wolf
    sheep = (1 if land[a][b] == "k" else 0)
    wolf = (1 if land[a][b] == "v" else 0)

    canEscape = False
    land[a][b] = '#'

    def in_range(x, y):
        return x in range(row) and y in range(col)

    while len(q) > 0:
        location = q.popleft()
        x, y = location[0], location[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                canEscape = True
                continue

            if land[nx][ny] != '#':
                sheep += (1 if land[nx][ny] == 'k' else 0)
                wolf += (1 if land[nx][ny] == 'v' else 0)
                land[nx][ny] = "#"
                q.append((nx, ny))
    #if land doesnt belong to any sector, the sheep and wolf stay alive
    if canEscape:
        sheep_count += sheep
        wolf_count += wolf
    else:
        if sheep > wolf: # if more sheep than wolf, sheep survives
            sheep_count += sheep
        else: # if more wolf than sheep, wolf eats sheep
            wolf_count += wolf
    print(sheep_count, wolf_count)
    for i in range(row):
        print(land[i])
land = []
backyard = [0] * 500
row, col = map(int, input().split())

for i in range(row):
    land.append(list(input()))

for i in range(row):
    for j in range(col):
        if land[i][j] != '#':
            BFS(i, j)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))