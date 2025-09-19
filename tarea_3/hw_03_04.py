

def cuatro(a):
    n = len(a)      # T(n) = 1
    total = 0       # T(n) = 1
    n = (n * 2) / 2     # T(n) = 1
    for i in range(n):      # T(n) = n
        basura = 1      # T(n) = 1
        nada = 0        # T(n) = 1
        i = i       # T(n) = 1
        for j in range(n):      # T(n) = n
            basura2 = 1     # T(n) = 1
            otra_cosa = 2       # T(n) = 1
            j = j       # T(n) = 1
            for k in range(n):      # T(n) = n
                total = total       # T(n) = 1
                k = k       # T(n) = 1
                j = j       # T(n) = 1
                total += a[i] + a[j] + a[k]     # T(n) = 1
    return total        # T(n) = 1


