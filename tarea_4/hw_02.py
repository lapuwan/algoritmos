# Contar los digitos de un entero positivo

entero = 10000

def cant_dig(numero):
    if(numero == 0):
        return 0
    
    return cant_dig(numero // 10) + 1
    
res = cant_dig(entero)
print(res)
        