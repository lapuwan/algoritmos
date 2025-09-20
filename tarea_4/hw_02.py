# Contar los digitos de un entero positivo

# Inicio del Método

def cant_dig(numero):
    if(numero == 0):
        return 0
    
    return cant_dig(numero // 10) + 1

# Fin del Método   

# Inicio de Pruebas

entero = 123456789 
res = cant_dig(entero)
print(res)
        