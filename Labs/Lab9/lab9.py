def power(x,n):
    if n == 1:
        return x
    else:
        return(x*(power(x,n-1)))

def interleave(L1,L2):
    if (len(L1) == 0):
        return []
    else:
        return[L1[0],L2[0]]+ interleave(L1[1:],L2[1:])

def reverse_rec(L,i = 0):
    if len(L)//2 == i:
        return L
    else:
        L[i], L[-1-i] = L[-1-i],L[i]
        return reverse_rec(L,i+1)

def print_L(L,i=0):
    if len(L)//2 == i:
        print('')
    else:
        print(L[len(L)//2],L[len(L)//2-(i+1)],L[len(L)//2+(i+1)],end = " ")
        print_L(L,i+1)

def is_balanced(s):
    start = min(s.find("("),s.find(")"))
    end = max(s.rfind(")"),s.rfind("("))
    if start != -1 and end != -1:
        return is_balanced(s[start+1:end])
    elif start == -1 and end == -1:
        return True
    else:
        return False

print(power(2,3))