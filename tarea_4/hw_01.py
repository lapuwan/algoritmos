# Crear una lista de enteros en Python y realizar la suma con recursividad, el caso base es cuando la lista esta vacia.

# Inicio del Método

def suma(arr):
    if (len(arr) == 0):
        return 0
    return arr.pop() + suma(arr)

# Fin del Método

# Inicio de Pruebas

numeros = [1,2,3,4,5,6]
res = suma(numeros)
print(res)
    