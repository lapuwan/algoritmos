# Verificar si una cadena es Palíndromo con recursividad

# Inicio del Método

# n es obligatoriamente cero
# z es el tamaño de la cadena
def es_palindromo(cadena, n,z):
    if cadena[n] != cadena[z-1]:
        return False
    elif n == z or n > z:
        return True        
    else:
        return es_palindromo(cadena, n+1, z-1 )

# Fin del Método   

# Inicio de Pruebas
cade = "reconocer"
size = len(cade)
yes_or_no = es_palindromo(cade, 0, size)
print(yes_or_no)
