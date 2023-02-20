def f(L):
    for i in range(len(L)):
        pass

# O(n), n = len(L)

def g(L):
    for i in range(int(len(L)**.5)):
        pass

# O(sqrt(n))

def log10(n):
    res = 0
    while n > 1:
        n //= 10
        res += 1
    return res

# O(log(n))

def square(n):
    res = 0
    for i in range(n):
        res += n
    return res

# O(n)

def h(L):
    for i in range(len(L)):
        for j in range(len(L)//2):
            pass

    # k1 * n*n/2 time

    for i in range(len(L)*1000):
        pass

    # k2 * n time

    # Total: k1*n^2/2 + k2*n time
    #        proportional to n^2 for large n
    # O(n^2)


# Fermat's Last Theorem:
# i^p + j^p = k^p does not have integer solutions for p > 2
