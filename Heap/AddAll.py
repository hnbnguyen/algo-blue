import heapq

def solve(n, arr):
    total = 0
    heap = []
    for item in arr:
        heapq.heappush(heap, item)
    while(len(heap) > 1):
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        total += cost
        heapq.heappush(heap, cost)
    print(total)


while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    solve(n, arr)
