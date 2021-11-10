import sys
import time
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    ans = 0
    # iterating through the list with j index
    # i starts with 0, as j iterate through the list, temp list add a new element at
    # index j to the temp list, if there is repeating element, reset the temp list and
    # reassess ans = max(ans, j-i), and i become what j is
    l = [s[i] for i in range(len(s))]
    i = 0
    tempList = []
    for j in range(len(l)):
        if l[j] not in tempList:
            tempList.append(l[j])
        else:
            ans = max(ans, j - i)
            i = j + 1
            tempList = []
    return ans

s = input()
print(lengthOfLongestSubstring(s))

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))