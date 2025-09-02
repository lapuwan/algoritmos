# TAREA 1: Búsqueda lineal
list_01 = [3,8,4,7,9,5,2]       # T(n) = n   S(n) = n

valor_A_Buscar = 100      # T(n) = 1   S(n) = 1

def busq_lineal (arreglo, valor):       # S(n) = 1
    
    contador = 0        # T(n) = 1   S(n) = 1
    for i in arreglo:       # T(n) = n   S(n) = 1
        contador += 1       # T(n) = 1
        if(i == valor):     # T(n) = 1
            return contador, True       # T(n) = 1
    return contador, False      # T(n) = 1

contador, encontrado = busq_lineal(list_01, valor_A_Buscar)     # T(n) = 1   S(n) = 2
if encontrado:      # T(n) = 1
    print(f"Número {valor_A_Buscar} encontrado.\nNúmero de comparaciones: {contador}")      # T(n) = 1
else:
    print(f"Número {valor_A_Buscar} no encontrado.\nNúmero de comparaciones: {contador}")       # T(n) = 1

# T(n) = n + 1 + 1 + n + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = [2n + 10]
# S(n) = n + 1 + 1 + 1 + 1 + 2 = [n + 6]