def sorting(ar):
    if len(ar) <= 1:
        return ar
    left, equal, right = partition(ar)
    merging_arr = sorting(left) + equal + sorting(right)
    print (' '.join(str(e) for e in merging_arr))       
    return merging_arr
def partition(ar):
    left, equal, right=[],[ar[0]],[]
    for elem in ar[1:]:
        if elem < ar[0]:
            left.append(elem)
        elif elem == ar[0]:
            equal.append(elem)        
        else:
            right.append(elem)

    return left, equal, right
n = input()
ar = list(map(int,input().rstrip().split()))
sorting(ar)
