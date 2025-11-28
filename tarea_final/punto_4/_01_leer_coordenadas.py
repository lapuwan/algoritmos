def leer_coordenadas(link):
    coords = []

    with open(link, "r") as archivo:
        for linea in archivo:
            x, y = map(int, linea.split())
            coords.append((x, y))

    #print(coords)

    coords.pop() 
    coords_ordenadas = sorted(coords, key=lambda p: (p[0], p[1]))
    
    return coords_ordenadas