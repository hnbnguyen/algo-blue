# input: A directed graph
# output: Maximum number of bombs that can explode in one trigger

# suppose I choose bomb 1 to trigger --> how many bombs eventually explodes?
# no. of exploding bombs = number of reachable nodes (starting from 1)

# create adjacency list
# DFS to go through each bomb and count how many reachable nodes are there
# return the maximum number of explosions

# brute force algorithm:
# try every starting bombs, to see how much will explode if we start from that bomb
# the number of exploding bombs is the number of reachable nodes starting from (start bomb)


# 1 -> 2 -> 3 -> 4
# |
# 5
# |
# 6

# final algorithm:
# try every single starting bombs
# for each starting bomb: count how many reachable bombs from this starting bomb
graph = [[] for i in range(10001)]
n, m = map(int, input().split())
max_explosion = 0
num_bomb = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def DFS(u):
    visited[u] = True

    global num_bomb
    num_bomb += 1

    for bomb in graph[u]:
        if visited[bomb] == False:
            DFS(bomb)

for start_bomb in range(1, n+1):
    visited = [False for i in range(10001)]
    num_bomb = 0
    # DFS from start_bomb, count how many vertices are reachable from start_bomb
    DFS(start_bomb)
    max_explosion = max(max_explosion, num_bomb)

print(max_explosion)


