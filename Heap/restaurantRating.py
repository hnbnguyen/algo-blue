import sys
import time
import heapq
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
# overall time complexity: Onlogn
# if 1 is called: add new reviews to a heap (Ologn)
# if 2 is called: get the length of the heap, n, (On), and then the
# number of displayed, floor(n/3), then pull out that many item (Ologn)
# push everything back into the heap after displayed
t = int(input())
arr = []
for i in range(t):
    request = input()
    if len(request) == 1:
        n = len(arr)
        display = n//3
        arr = sorted(arr, reverse = True)
        top = arr[:display]
        print(top)
        if len(top):
            print(top[-1])
        else:
            print('No reviews yet')
    else:
        call, rating = map(int, request.split())
        arr.append(rating)
# heap = []
# for i in range(t): #On
#     request = input()
#     if len(request) == 1: # 2 is called
#         n = len(heap)
#         display = n//3
#         top = heapq.nlargest(display, heap) #Ologn * display
#         if len(top) == 0:
#             print("No reviews yet")
#         else:
#             print(top[-1])
#     else:
#         call, rating = map(int,request.split())
#         heapq.heappush(heap, rating) # Ologn


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))