
# a es una lista

def tres(a):
    cnt = 0     # T(n) = 1
    n = len(a)      # T(n) = 1
    for i in range(n):      # T(n) = n 
        for j in range(i+1):        # T(n) = m
            cnt += 1        # T(n) = 1
    return cnt      # T(n) = 1



