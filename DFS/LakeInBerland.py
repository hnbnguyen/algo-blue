import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

row, col, k = map(int, input().split())
land = []
for i in range(row):
    land.append(input())

visited = [[False for c in range(col)] for r in range(row)]
s = []

# count all the connected components and their size
# if lake_count == k, stop
# if need to remove lake, start with with wiping out the lake with the least amount of square

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))