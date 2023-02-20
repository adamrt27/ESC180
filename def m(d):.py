def selection_sort(L):
    for i in range(len(L)):
        cur_ind = i
        for j in range(i+1,len(L)):
            if L[j] < L[cur_ind]:
                cur_ind = j
        L[cur_ind], L[i] = L[i], L[cur_ind]
    return L

def merge_sort(L):
    if len(L) == 2:
        if L[0] > L[1]:
            return [L[1], L[0]]
    else:
        mid = len(L)//2
        return [merge_sort(L[mid:]),merge_sort(L[:mid])]

print(merge_sort([3,2,4,5,6,1,2,3]))