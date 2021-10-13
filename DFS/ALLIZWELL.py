t = int(input())
key = list("ALLIZZWELL")

for case in range(t):
    found = False
    wordmap = []
    r, c = map(int, input().split())
    visited  = [[False for i in range (c)] for j in range(r)]
    for i in range(r):
        wordmap.append(list(input()))
    input()

    # dfs(coordinate, current character):
    #   visited[coordinate] = True
    #     try all neighbors:
    #        if (visited[neighbor] == False) and (wordmap[neighbor] = next character)
    #           DFS(neighbor, next character)
    #   visited[coordinate] = False

    def DFS(x, y, curChar):
        visited[x][y] = True
        curChar += 1
        dx = [0, 0, 1, 1, -1, -1, -1, 1]
        dy = [-1, 1, 0, 1, 0, 1, -1, -1]

        for i in range(8):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if n_x in range(0, r) and n_y in range(0, c) and (visited[n_x][n_y] == False) and (wordmap[n_x][n_y] == key[curChar]):
                if curChar == len(key) - 1:
                    global found
                    found = True
                    return
                DFS(n_x, n_y, curChar)

        visited[x][y] = False

    for i in range(r):
        for j in range(c):
            if wordmap[i][j] == "A" and visited[i][j] == False:
                DFS(i, j, 0)
    print("YES" if found else "NO")