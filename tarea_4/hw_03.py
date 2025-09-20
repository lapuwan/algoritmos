# Eliminar de un ADT pila el valor en la posición media.

# Creación de la clase Pila

class Pila:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



# Inicio del Método

def eliminar_medio_rec(pila, k=None):
    if k is None:
        k = pila.size() // 2   # posición del medio

    # caso base → si estamos en el medio, eliminarlo
    if k == 0:
        pila.pop()
        return

    # guardar el tope
    temp = pila.pop()

    # llamada recursiva
    eliminar_medio_rec(pila, k - 1)

    # al regresar, volvemos a poner el elemento
    pila.push(temp)
        
# Fin del Método

# Inicio de Pruebas

p = Pila()

for x in [1, 2, 3, 4, 5, 6,7,8,9,10]:
    p.push(x)

res = eliminar_medio_rec(p)
print(p)