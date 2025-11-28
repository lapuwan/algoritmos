from _01_leer_coordenadas import leer_coordenadas
import time

#  FUNCION PARA CALCULAR AREA DE TRIANGULO
def area_triangulo(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(
        x1*(y2 - y3) +
        x2*(y3 - y1) +
        x3*(y1 - y2)
    ) / 2



#  LEER ARCHIVO campo.in
puntos = leer_coordenadas("punto_4/campo.in")


n = len(puntos)
max_area = 0
mejor = None


#      FUERZA BRUTA O(n³)
inicio = time.time()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = area_triangulo(puntos[i], puntos[j], puntos[k])
            if area > max_area:
                max_area = area
                mejor = (puntos[i], puntos[j], puntos[k])

fin = time.time()


#      ESCRIBIR ARCHIVO campo.out

with open("campo.out", "w") as f:
    if mejor is not None:
        for p in mejor:
            f.write(f"{p[0]} {p[1]}\n")
        print("archivo campo.out creado con éxito por fuerza bruta")
        print("     Tiempo de ejecución:", fin - inicio, "segundos")
