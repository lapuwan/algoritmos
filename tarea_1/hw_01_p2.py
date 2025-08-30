list_01 = [8,2,6,23,4,345,9,1]

k = 10
set_ = set()
contador = 0
is_true = False

for i in list_01:
    complemento= k - i
    if (complemento in set_):
        print(f"Si existe un par: {complemento} + {i}")
        contador += 1
        is_true = True
    else:
        set_.add(i)

print("--------------------------")
if(is_true == False):
    print(f"No hay pares que den como suma {k}")
elif(contador == 1):
    print(f"Hay sólo 1 par")
else:
    print(f"Hay {contador} pares")