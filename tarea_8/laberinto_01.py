def leer_laberinto(archivo):

    with open(archivo, 'r') as f:
        filas = int(f.readline().strip())
        columnas = int(f.readline().strip())
        laberinto = []
        for _ in range(filas):
            fila = f.readline().strip().split(",")
            laberinto.append(fila)
    return laberinto, filas, columnas


def encontrar_entrada_salida(laberinto):
    entradas = []
    salidas = []

    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == 'E':
                entradas.append((i, j))
            elif celda == 'S':
                salidas.append((i, j))
                
    if len(entradas) != 1 or len(salidas) != 1:
        print("Error: debe haber exactamente una entrada (E) y una salida (S).")
        print(f"Entradas encontradas: {entradas}")
        print(f"Salidas encontradas: {salidas}")
        return None, None

    return entradas[0], salidas[0]



def resolver_laberinto_por_backtracking(laberinto, inicio, fin):
    
    filas, columnas = len(laberinto), len(laberinto[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pila = [(inicio, [inicio])]  
    visitados = set()

    while pila:
        (x, y), ruta = pila.pop()

        if (x, y) == fin:
            return ruta

        if (x, y) in visitados:
            continue
        visitados.add((x, y))

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if laberinto[nx][ny] in ['0', 'S'] and (nx, ny) not in visitados:
                    pila.append(((nx, ny), ruta + [(nx, ny)]))
    return None


def imprimir_ruta(ruta):
    print("numero de celdas que conforman la ruta: ", len(ruta))
    print("Ruta encontrada:")
    for paso in ruta:
        print(paso)


def hay_camino_o_no(entrada, salida, laberinto):
        if not entrada or not salida:
            print("Error: no se encontró la entrada o la salida.")
            return

        ruta = resolver_laberinto_por_backtracking(laberinto, entrada, salida)

        if ruta:
            imprimir_ruta(ruta)
        else:
            print("No se encontró una ruta hacia la salida.")



""" Inicio de la lectura del archivo .txt y uso de los métodos """

archivo = "archivo_03.txt"
laberinto, filas, columnas = leer_laberinto(archivo)

entrada, salida = encontrar_entrada_salida(laberinto)
hay_camino_o_no(entrada, salida, laberinto)
    

