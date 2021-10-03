def solve(country, graph):
    stack = []
    visited = [False for i in range(n)]
    dist = [0 for i in range(n)]
    stack.append(0)
    visited[0] = True

    while(len(stack) > 0):
        location = stack.pop()
        for i in graph[location]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
                dist[i] = dist[location] + 1
    #country with min distance from bishu
    #take the one with smaller id

    ans = country[0]
    # try every countries

    for i in country:
        if dist[i] < dist[ans]: # if dist[i] is smaller --> take country i (instead of ans)
            ans = i
        elif dist[i] == dist[ans]:    # if distance is the same --> take smaller id
            ans = min(ans, i)
    print(ans + 1)
    # print(dist)

n = int(input())
graph = [[] for i in range(n)]
# remember to check for index
for i in range(n-1):
    u, v = map(int, input().split()) # 1-indexed
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)# bi-directional

country = []
q = int(input())
for i in range(q):
    country.append(int(input())-1)
solve(country, graph)




