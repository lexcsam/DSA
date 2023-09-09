#https://www.hackerrank.com/challenges/qheap1/problem
import heapq

Q = input()
heap = []
delset = set()
for _ in range(int(Q)):
    q = input()
    if len(q) == 1:
        while heap[0] in delset:
            heapq.heappop(heap)
        print(heap[0])
    else:
        n1 = int(q[0])
        n2 = int(q[2:])
        if n1 == 1:
            heapq.heappush(heap, n2)
        else:
            delset.add(n2)
##################################################
############SOLUTION-2############################

def heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)



def insert_element(heap, element):
    heap.append(element)
    n = len(heap)
    i = n - 1

    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2



def delete_element(heap, element):
    n = len(heap)
    i = heap.index(element)

    heap[i], heap[n - 1] = heap[n - 1], heap[i]
    heap.pop()

    heapify(heap, n - 1, i)



def print_minimum(heap):
    if len(heap) > 0:
        print(heap[0])



heap = []
queries = int(input())

for _ in range(queries):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        element = int(query[1])
        insert_element(heap, element)
    elif query_type == 2:
        element = int(query[1])
        delete_element(heap, element)
    elif query_type == 3:
        print_minimum(heap)
