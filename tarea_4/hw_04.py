# Verificar si una cadena es Palíndromo con recursividad

# Inicio del Método

def es_palindromo(cadena, n = None,z = None):
    if n == None:
        n = 0
        z = len(cadena)
        
    if cadena[n] != cadena[z-1]:
        return False
    elif n == z or n > z:
        return True        
    else:
        return es_palindromo(cadena, n+1, z-1 )

# Fin del Método   

# Inicio de Pruebas

cade = "reconocer"
yes_or_no = es_palindromo(cade)
print(yes_or_no)
