def fact_while(n):
    # cur_product = (i-1)!
    # Invariant (some property of the variables that
    # always holds)
    cur_prod, i = 1, 1

    while i != n+1:
        cur_prod *= i
        i += 1
    
    return cur_prod

def fact_rec(n):

    if n == 0:
        return 1
    else:
        return fact_rec(n-1)*n

def fact_iter(n, cur_prod = 1, i = 1):
    if i == n+1:
        return cur_prod
    return fact_iter(n, cur_prod*i, i+1)

def fact_kinda_rec(n):
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    res = 1
    while len(stack) > 0:
        res *= stack.pop()
    return res

# Merge Sort
# CPython's sort and sorted use TimSort (variation of Merge Sort)

# [10, 2, 4, 15, 20, 1, 2]
# 1. Sort the first half
# 2. Sort the second half
# 3. Merge the two sorted halves

def merge_inefficient(L1, L2):
    return sorted(L1 + L2)

# [5, 10, 12, 15]
# [4, 4.5, 7, 13]
# res = [4, 4.5, 5, 7, 10, 12, 13, 15]

def merge(L1, L2):
    '''Return a sorted version of L1 + l2
    assume L1 and L2 are sorted in non-increasing
    order'''
    ind1 = 0
    ind2 = 0
    res = []
    while ind1 < len(L1) and ind2 < len(L2):
        if L1[ind1] < L2[ind2]:
            res.append(L1[ind1])
            ind1 += 1
        else:
            res.append(L2[ind2])
            ind2 += 1
    res.extend(L1[ind1:])
    res.extend(L2[ind2:])
    
    return res

    # In total, we'll append len(L1)+len(L2) elements to
    # merged, and the appends are taking up most of the runtime
    # so the runtime is O(len(L1)+len(L2))


def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    
    mid = len(L)//2
    return merge(merge_sort(L[:mid]),merge_sort(L[mid:]))

print(merge_sort([69,2,6,5,4,3,99]))