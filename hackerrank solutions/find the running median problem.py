#https://www.hackerrank.com/challenges/find-the-running-median/problem

import heapq
def runningMedian(a):
    low = []    
    high = []   
    ans = []    
    for i in range(len(a)):

        if i == 0 or a[i] >= med:
            heapq.heappush(high, a[i])
        else:
            heapq.heappush(low, a[i] * -1)
        if len(high) - len(low) > 1:
            heapq.heappush(low, heapq.heappop(high) * -1)
        elif len(low) > len(high):
            heapq.heappush(high, heapq.heappop(low) * -1)
        if len(high) > len(low):
            med = float(high[0])
        else:
            med = float((high[0] - low[0]) / 2)
        ans.append(med)
    return ans