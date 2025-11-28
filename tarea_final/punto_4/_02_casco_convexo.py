
def cross(o, a, b):
    # Producto cruzado: (OA x OB)
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(coords):
    # Ordenar los puntos por x, y
    coords = sorted(coords)

    lower = []
    for p in coords:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(coords):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Quitar el último de cada lista (porque se repiten)
    lower.pop()
    upper.pop()

    # Concatenar lower + upper
    return lower + upper

