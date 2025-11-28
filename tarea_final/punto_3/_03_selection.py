def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Suponemos que el elemento actual es el mínimo
        min_index = i

        # Buscamos el verdadero mínimo en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiamos el mínimo encontrado con la posición actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


