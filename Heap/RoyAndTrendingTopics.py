import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

# reading the test case and multiply it by its respective score increment
t = int(input())
arr = []
for i in range(t):
    idx, z, p, l, c, s = map(int, input().split())
    zi = (p * 50) + (l * 5) + (c * 10) + (s * 20)
    change = zi - z
    arr.append([idx, zi, change])
arr = sorted(arr, key=lambda x: (-x[2], -x[0]))

for i in range(5):
    print(arr[i][0], arr[i][1])
    


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))