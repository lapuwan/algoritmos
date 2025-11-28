from _01_bubble_sort import bubble_sort
from _02_merge_sort import merge_sort
from _03_selection import selection_sort
from _04_bogo_sort import bogo_sort
import time


# ¿ESCOGER QUÉ NÚMERO DE ELEMENTOS ORDENAR?

print("¿Qué archivo quieres ordenar?")

print("Diez números: ingresa \"1\" en consola")
print("Cien números: ingresa \"2\" en consola")
print("Mil números: ingresa \"3\" en consola")
print("Diez mil números: ingresa \"4\" en consola")
print("Cien mil números: ingresa \"5\" en consola")
numero = int(input("Ingresa el número: "))

archivo = ""
lista_original = []


if numero == 1:
    archivo = "diez_numeros.txt"
elif numero == 2:
    archivo = "cien_numeros.txt"
elif numero == 3:
    archivo = "mil_numeros.txt"
elif numero == 4:
    archivo = "diez_mil_numeros.txt"
else:
    archivo = "cien_mil_numeros.txt"
    
    
# LEEMOS EL ARCHIVO
with open(archivo, "r") as f:
    lista_original = [int(x) for x in f.read().split()]

# BUBBLE SORT
lista_bubble = lista_original.copy()
inicio1 = time.time()
bubble_sort(lista_bubble)
fin1 = time.time()
print("BUBBLE SORT")
print("     Tiempo de ejecución:", fin1 - inicio1, "segundos")

# MERGE SORT
lista_merge = lista_original.copy()
inicio2 = time.time()
merge_sort(lista_merge)
fin2 = time.time()
print("MERGE SORT")
print("     Tiempo de ejecución:", fin2 - inicio2, "segundos")

# SELECTION SORT
lista_selection = lista_original.copy()
inicio3 = time.time()
selection_sort(lista_selection)
fin3 = time.time()
print("SELECTION SORT")
print("     Tiempo de ejecución:", fin3 - inicio3, "segundos")


# BOGO SORT
print("BOGO SORT")

if archivo == "diez_numeros.txt":
    lista_bogo = lista_original.copy()
    inicio4 = time.time()
    resultado, intentos = bogo_sort(lista_bogo)
    fin4 = time.time()
    
    print("     Intentos necesarios:", intentos)
    print("     Lista ordenada:", resultado)
    print("     Tiempo de ejecución:", fin4 - inicio4, "segundos")
else:
    print("     No es posible ejecutar el algoritmo Bogo Sort porque el número de elementos es muy grande")


