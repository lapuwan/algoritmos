# Eliminar de un ADT pila el valor en la posición media.

# Inicio del Método

def eliminar_medio(pila, k):

    if k == 0:
        pila.pop()
        return

    temp = pila.pop()

    eliminar_medio(pila, k - 1)

    pila.push(temp)
        
# Fin del Método

# Inicio de Pruebas



p = [1, 2, 3, 4, 5, 6,7,8,9,10]

size = len(p) // 2
res = eliminar_medio(p, size)
print(p)