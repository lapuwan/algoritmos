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



