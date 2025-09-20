# Eliminar de un ADT pila el valor en la posición media.

# Inicio del Método

def eliminar_medio(pila, k):
    if k == len(pila):
        k //= 2
    if len(pila) <=2:
        return
    if k == 0:
        pila.pop()
        return

    temp = pila.pop()

    eliminar_medio(pila, k - 1)

    pila.append(temp)
        
# Fin del Método

# Inicio de Pruebas

p = [1,2,3,4,5,6,7,8,9,10,11]

size = len(p)
res = eliminar_medio(p, size)
print(p)