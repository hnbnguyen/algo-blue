import heapq

def solve(n, arr):
    heap = []
    for i in range(n):
        heapq.heappush(heap, -arr[i])
        if len(heap) < 3:
            print(-1)
        else:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            third = heapq.heappop(heap)
            print(-(first * second * third))
            heapq.heappush(heap, first)
            heapq.heappush(heap, second)
            heapq.heappush(heap, third)

# situation: heapq implements a minheap, not maxheap as needed
# workaround: negate elements, so that smallest becomes largest, and vice-versa

n = int(input())
arr = list(map(int, input().split()))
solve(n, arr)