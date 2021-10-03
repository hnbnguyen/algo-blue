import sys

sys.setrecursionlimit(10**6)

def DFS(f):
    visited[f] = True
    for g in graph[f]:
        if visited[g] == False:
            DFS(g)

t = int(input())
for i in range(t):
    n = int(input())
    q = int(input())
    graph = [[] for k in range(n)]

    for j in range(q):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    friend_group = 0
    visited = [False for f in range(n)]
    for l in range(n):
        if visited[l] == False:
            friend_group += 1
            DFS(l)
    print(friend_group)
