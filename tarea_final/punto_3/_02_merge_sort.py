def merge_sort(arr):
    
    
    # Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    izquierda = arr[:mid]
    derecha = arr[mid:]

    # Ordenar cada mitad recursivamente
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Combinar las dos mitades
    return merge(izquierda, derecha)


def merge(left, right):
    resultado = []
    i = j = 0

    # Mezclar mientras haya elementos en ambas listas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(left[i:])
    resultado.extend(right[j:])

    return resultado

