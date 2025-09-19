# Probar los 5 códigos

def uno(n):
    s = 0       # T(n) = 1
    for i in range(n+1):        # T(n) = n
        basura = i      # T(n) = 1
        s += i      # T(n) = 1
        i = i       # T(n) = 1
    return s        # T(n) = 1

num = uno(10)
print(num)
