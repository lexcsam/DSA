#https://www.hackerrank.com/challenges/quicksort1/problem


def partition(array, low, high):
    pivot = array[low]
    start = low + 1
    end = high
    while True:
        while start <= end and array[end] >= pivot:
            end = end - 1
        while start <= end and array[start] <= pivot:
            start = start + 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break
    array[low], array[end] = array[end], array[low]
    return end
def quick_sort(array, start, end):
    if start < end:
        idx = partition(array, start, end)
        quick_sort(array, start, idx-1)
        quick_sort(array, idx+1, end)
n=int(input())
arr1= list(map(int,input().split()))
quick_sort(arr1, 0, len(arr1)-1)
for i in arr1:
    print(i,end=" ")
