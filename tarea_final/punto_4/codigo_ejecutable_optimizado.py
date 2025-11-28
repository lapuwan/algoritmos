from _01_leer_coordenadas import leer_coordenadas
from _02_casco_convexo import convex_hull
from _03_tres_punteros import max_area_triangle

# PASO 1: ORDENAR LAS COORDENADAS Y ELIMINAR LA COORDENADA -1 -1
coord_ord = leer_coordenadas("coordenadas.txt")
#primeros_diez = coord_ord[:10]
#print(primeros_diez)
#print(coord_ord)

# PASO 2: ENCONTRAR LAS COORDENADAS QUE CONFORMAN EL CASCO CONVEXO
hull = convex_hull(coord_ord)

# PASO 3: TRES PUNTEROS
# Encontrar las coordenadas del triángulo y el aréa máxima
coord_triangulo, area = max_area_triangle(hull)

# IMRIMIMOS LOS RESULTADOS (COORDENADAS Y EL AREA)
print(f"Las coordenadas del triángulo es: {coord_triangulo}")
print(f"El área es de: {area}")
print()

# CREAMOS EL ARCHIVO campo.out con las coordenadas del triángulo
with open("campo.out", "w") as archivo:
    for x, y in coord_triangulo:
        archivo.write(f"{x} {y}\n")
    print("archivo campo.out creado con éxito con optimización")