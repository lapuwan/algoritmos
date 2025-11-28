import random

def esta_ordenado(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    intentos = 0
    while not esta_ordenado(arr):
        random.shuffle(arr)
        intentos += 1
    return arr, intentos


# Ejemplo de uso
#lista = [3, 1, 35,2,5,8,4,10,24]
#resultado, intentos = bogo_sort(lista)
#print("Lista ordenada:", resultado)
#print("Intentos necesarios:", intentos)
