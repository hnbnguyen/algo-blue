import sys
import time
from collections import deque
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def solve(sam, lock):
    dist = [-1] * 100001
    q = deque()
    q.append(sam)
    dist[sam] = 0

    while len(q) >0:
        now = q.popleft()
        for num in other:
            #get multiplication
            new = (num * now) % 100000
            # if the distance not registered, dist = now's dist + 1
            if dist[new] == -1:
                dist[new] = dist[now] + 1
                # add the multiplication result to queue
                q.append(new)

            # if now == target then return the step needs to get to now
            if now == lock:
                print(dist[now])
                return
    print(-1)


sam, lock = map(int, input().split())
n = int(input())
other = list(map(int, input().split()))
solve(sam, lock)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))