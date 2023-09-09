#https://www.hackerrank.com/challenges/insertionsort2/problem

def recursive_print(ar):
    if ar == []:
        return ""
    return str(ar[0]) + " " + recursive_print(ar[1:])
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=a[j]
            j=j-1
        a[j+1]=key
        print(recursive_print(arr))
n=int(input())
a=list(map(int,input().split(" ")))


insertion_sort(a)
