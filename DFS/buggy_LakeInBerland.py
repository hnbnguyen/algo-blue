import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


def solve(r, c):
    # count all the connected components and their size
    visited = [[False for c in range(col)] for r in range(row)]
    num_lake = 0
    lake_size = []
    lake_id = 0

    def not_ocean(x, y):
        return 0 < x < r -1 and 0 < y < c - 1

    def is_water_cell(x, y):
        return land[x][y] == "."

    for i in range(r):
        for j in range(c):
            if visited[i][j] is False and is_water_cell(i, j):
                lake_size.append([[i, j], 1])
                num_lake += 1
                stack = []
                visited[i][j] = True
                stack.append([i, j])
                is_ocean = False

                while len(stack) > 0:
                    dx = [0, 0, 1, -1]
                    dy = [1, -1, 0, 0]
                    location = stack.pop()

                    for h in range(4):
                        nx = location[0] + dx[h]
                        ny = location[1] + dy[h]

                        if nx in range(r) and ny in range(c) and visited[nx][ny] == False and is_water_cell(nx, ny):
                            if not not_ocean(nx, ny):
                                is_ocean = True
                            lake_size[lake_id][1] += 1
                            visited[nx][ny] = True
                            stack.append([nx, ny])
                if is_ocean:
                    num_lake -= 1
                    lake_size.pop()
                print(is_ocean)
                print('at point', i, j, ': ',num_lake)
                lake_id += 1
    if num_lake == k:
        return
    num_remove = num_lake - k
    # if need to remove lake, start with with wiping out the lake with the least amount
    # of square
    sorted_size = sorted(lake_size, key = lambda x: x[1], reverse = True)
    for y in range(num_remove):
        start = sorted_size.pop()[0]
        new_str = ''
        for r in range(len(land[start[0]])):
            if r == start[1]:
                new_str = new_str + "*"
            else:
                new_str = new_str + land[start[0]][r]
        land[start[0]] = new_str
        print(new_str)
        stack2 = [start]

        while len(stack2) > 0:
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            location = stack2.pop()

            for h in range(4):
                nx = location[0] + dx[h]
                ny = location[1] + dy[h]

                if nx in range(r) and ny in range(c) and is_water_cell(nx, ny):
                    lake_size[lake_id][1] += 1
                    new_str = ''
                    for r in range(len(land[nx])):
                        if r == ny:
                            new_str = new_str + "*"
                        else:
                            new_str = new_str + land[nx][r]
                    land[nx] = new_str
                    stack2.append([nx, ny])

row, col, k = map(int, input().split())
land = []
for l in range(row):
    land.append(input())
solve(row, col)
print(land)





start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))