def dos(n):
    cnt = 0     # T(n) = 1
    for _ in range(n):      # T(n) = n
        j = n       # T(n) = 1
        j = j       # T(n) = 1
        while j > 1:        # T(n) = log_2(m)
            j //= 2     # T(n) = 1
            j = j       # T(n) = 1
            cnt += 1        # T(n) = 1
            cnt = cnt       # T(n) = 1
    print("fin del for")        # T(n) = 1
    return cnt      # T(n) = 1




print(dos(10))