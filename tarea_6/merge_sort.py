def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Dividimos la lista en dos partes
        izquierda = merge_sort(izquierda)
        derecha = merge_sort(derecha)
        
        # Ordenamos ambas partes
        combinar(izquierda, derecha, lista)

    return lista

def combinar(izquierda, derecha, lista):
    i = j = k = 0

    # Hacemos las comparaciones entre los elementos de ambas partes
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Agregar los elementos restantes
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1
        
    return lista

# Ejemplo:

nums = [47, 3, 89, 15, 62, 7, 28, 1, 91, 50, 13, 75, 2, 34, 68, 21]
print(merge_sort(nums))





#nums = [38, 27, 43, 3, 9, 82, 10]


