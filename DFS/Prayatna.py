def solve(numfriend, graph):
    friend_group = 0
    visited = [False for i in range(numfriend)]
    for i in range(numfriend):
        if visited[i] == False:
            stack = []
            stack.append(i)
            visited[i] = True
            while len(stack) > 0:
                friend = stack.pop()
                for j in graph[friend]:
                    if visited[j] == False:
                        visited[j] = True
                        stack.append(j)
            friend_group += 1
    print(friend_group)


    # for each vertex:
    #   if not visited:
    #     connected_component += 1
    #     dfs from vertex, and visit everything connected to it

t = int(input())
for i in range(t):
    n = int(input())
    q = int(input())
    graph = [[] for k in range(n)]

    for j in range(q):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    solve(n, graph)
