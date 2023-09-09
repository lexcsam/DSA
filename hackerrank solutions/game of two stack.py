#https://www.hackerrank.com/challenges/game-of-two-stacks/problem

def twoStacks(maxSum, a, b):
    i = j = running_sum = count = 0
    while i < len(a) and running_sum + a[i] <= maxSum:
        running_sum += a[i]
        i += 1
        count += 1
    while j < len(b) and i >= 0:
        running_sum += b[j]
        j += 1
        while i > 0 and running_sum > maxSum:
            i -= 1
            running_sum -= a[i]
        if running_sum <= maxSum and count < i + j:
            count = i + j  
    return count
test= int(input())
for i in range(test):
    a,b,c=map(int,input().split())
    stack1=list(map(int,input().split()))
    stack2=list(map(int,input().split()))
    print(twoStacks(c,stack1,stack2))
