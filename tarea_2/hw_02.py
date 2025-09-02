list_01 = [4, 1, 3, 7, 9, 100, 29, 10, 50]       # T(n) = n   S(n) = n

valor_A_Buscar = 400000      # T(n) = 1   S(n) = 1

def busq_lineal (arreglo, valor):       # S(n) = 1
    contador = 0        # T(n) = 1   S(n) = 1
    for i in arreglo:       # T(n) = n   S(n) = 1
        contador += 1       # T(n) = 1
        if(i == valor):     # T(n) = 1
            return contador, True       # T(n) = 1
    return contador, False      # T(n) = 1

def buscar_num (arreglo, valor):        # S(n) = 1
    contador, encontrado  = busq_lineal(arreglo, valor)     # T(n) = 1   S(n) = 2
    if encontrado:      # T(n) = 1
        print(f"Número {valor} encontrado.\nNúmero de comparaciones: {contador}")       # T(n) = 1
    else:
        print(f"Número {valor} no encontrado.\nNúmero de comparaciones: {contador}")        # T(n) = 1

buscar_num(list_01, valor_A_Buscar)     # T(n) = 1   S(n) = 1

# T(n) = n + 1 + 1 + n + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1= [2n + 11]
# S(n) = n + 1 + 1 + 1 + 1 + 1 + 2 + 1 = [n + 8]