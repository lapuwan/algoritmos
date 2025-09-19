# SOLUCIÓN USANDO UN set() // Implementado como tabla hash
# En este código se permite que un valor sumado por sí mismo sea k

# La lista
list_01 = [6,23,4,345,9,1]

#El valor k
k = 2

# Uso de un set()
set_ = set()

# Variable que nos permitirá imprimir en consola si no se encontró un par
is_true = False

print(f"Valor de k: {k}")

# Separador (uso estético)
print("--------------------------")

# Recorremos la lista
for i in list_01:
    complemento= k - i
    if (complemento in set_):
        print(f"Si existe un par: {complemento} y {i}")
        is_true = True
        break
    elif(i == k/2):
        print(f"El número {i} sumado por sí mismo nos da {k}")
        is_true = True
        break
    else:
        set_.add(i)

if(is_true == False):
    print(f"No hay al menos un par que den como suma {k}")