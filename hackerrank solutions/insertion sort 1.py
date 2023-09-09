#https://www.hackerrank.com/challenges/insertionsort1/problem


def recursive_print(ar):
    if ar == []:
        return ""
    return str(ar[0]) + " " + recursive_print(ar[1:])

def insertionSort(ar):
    last_index = len(ar) - 1
    last_index_value = ar[last_index] 
    while ar[last_index - 1] > last_index_value and last_index > 0:
        ar[last_index] = ar[last_index - 1]
        last_index -= 1
        print(recursive_print(ar))
    ar[last_index] = last_index_value
    print(recursive_print(ar))
    
input();
ar = input().split()
insertionSort(ar)



