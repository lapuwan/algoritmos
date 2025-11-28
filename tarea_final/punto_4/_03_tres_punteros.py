def triangle_area(a, b, c):
    return abs(
        (b[0] - a[0]) * (c[1] - a[1]) -
        (b[1] - a[1]) * (c[0] - a[0])
    ) / 2


def max_area_triangle(hull):
    n = len(hull)
    if n < 3:
        return None  # no existe triángulo

    max_area = 0
    best = None

    # Rotating calipers con i, j, k
    for i in range(n):
        j = (i + 1) % n
        k = (j + 1) % n

        while True:
            improved = False

            # Avanzar j
            while True:
                next_j = (j + 1) % n
                if next_j == i:
                    break
                if triangle_area(hull[i], hull[next_j], hull[k]) > triangle_area(hull[i], hull[j], hull[k]):
                    j = next_j
                    improved = True
                else:
                    break

            # Avanzar k
            while True:
                next_k = (k + 1) % n
                if next_k == i:
                    break
                if triangle_area(hull[i], hull[j], hull[next_k]) > triangle_area(hull[i], hull[j], hull[k]):
                    k = next_k
                    improved = True
                else:
                    break

            # Registrar si este triángulo es el mayor
            area = triangle_area(hull[i], hull[j], hull[k])
            if area > max_area:
                max_area = area
                best = (hull[i], hull[j], hull[k])

            if not improved:
                break

    return best, max_area
