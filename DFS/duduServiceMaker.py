import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

visited = [False] * 10005
graph = [[] for _ in range(10005)]


def DFS(u):
    visited[u] = 1

    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True
    visited[u] = 2
    return False


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    for i in range(n + 1):
        graph[i].clear()
        visited[i] = 0

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    is_loop = False

    for i in range(1, n + 1):
        if visited[i] == 0:
            is_loop = DFS(i)
            if is_loop:
                break

    print("YES" if is_loop else "NO")
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))