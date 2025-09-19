# Crear una lista de enteros en Python y realizar la suma con recursividad, el caso base es cuando la lista esta vacia.

numeros = [10,10,10,10,10]
size = len(numeros)
i = 0


def suma(arr):
    if (len(arr) == 0):
        return 0
    return arr.pop() + suma(arr)
    
    
    
res = suma(numeros)
print(res)
    