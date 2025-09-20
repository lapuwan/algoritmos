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

def eliminar_medio(pila, k):

    if k == 0:
        pila.pop()
        return

    temp = pila.pop()

    eliminar_medio(pila, k - 1)

    pila.push(temp)
        
# Fin del Método

# Inicio de Pruebas

p = Pila()

for x in [1, 2, 3, 4, 5, 6,7,8,9,10]:
    p.push(x)

size = p.size() // 2
res = eliminar_medio(p, size)
print(p)