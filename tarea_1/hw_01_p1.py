list_01 = [5,5,6,23,4,345]

k = 10
is_true = False
contador= 0
tamano_ls = len(list_01)

for i in range(tamano_ls):
    for j in range(i+1, tamano_ls):
        if (list_01[i] + list_01[j] == k):
            is_true = True
            print(f"{list_01[i]} + {list_01[j]} = {k}")
            contador +=1

print("----------------------------")
if (is_true == True):
    print(f"Sí hay pares que den como suma {k}")
    if (contador == 1):
        print(f"En total hay sólo 1 par")
    else:
        print(f"En total hay {contador} pares")
else:
    print(f"No hay parejas que den como suma {k}")