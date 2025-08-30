# SOLUCIÓN CON DOS FOR ANIDADOS
# En este código se permite que un valor sumado por sí mismo sea k

# Arreglo
list_01 = [5,7,23,4,345]

# Valor de k
k = 10
is_true = False

# Variable del tamaño de la lista
tamano_ls = len(list_01)

print(f"Valor de k: {k}")

# Separador (uso estético)
print("--------------------------")

for i in range(tamano_ls):
    for j in range(i, tamano_ls):
        if (list_01[i] + list_01[j] == k):
            is_true = True
            if(list_01[i] != list_01[j] ):
                print(f"El primer par encontrado fue: {list_01[i]} + {list_01[j]} = {k}")
            else:
                print(f"El número {list_01[i]} sumado por sí mismo nos da {k}")
            break
    if(is_true):
        break

if(is_true == False):
    print(f"No hay pares que den como suma {k}")
