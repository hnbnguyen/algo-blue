import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # traverse through the list of intervals
    # if the end of interval j is larger or equals to the beginning of
    # interval j + 1, then merge
    ans = []
    for j in range(len(intervals)):
        if j < len(intervals) - 1:
            end1 = intervals[j][1]
            end2 = intervals[j + 1][1]
            if end1 >= end2:
                #merge intervals
                ans.append([intervals[j][0], intervals[j+1][1]])
            else:
                ans.append(intervals[j])
    return ans

s = [[1,3],[2,6],[8,10],[15,18]]
print(merge(s))

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))