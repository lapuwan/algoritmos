
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Indicador para saber si hubo un intercambio
        intercambios = False

        # Recorrido de la lista
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                # Intercambio
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios = True

        # Si no hubo intercambios, ya está ordenado
        if not intercambios:
            break

    return arr

# Ejemplo de uso
#lista = [5, 1, 4, 2, 8]
#print(bubble_sort(lista))
