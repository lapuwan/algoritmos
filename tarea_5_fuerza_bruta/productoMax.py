# Dado un arreglo de enteros  A=[-9,3,5,−2,9,−7,4 ,8 , 6 ], encuentra dos números 
# en el arreglo cuyo producto sea el más alto empleando fuerza bruta.

arregloA = [-9,3,5,-2,9,-7,4 ,8 , 6]

productoMax = 0


for i in range(len(arregloA)):
    for j in range(len(arregloA)):
        if arregloA[i]*arregloA[j] > productoMax and i != j :
            prod = arregloA[i]*arregloA[j]
            productoMax = prod
            
print(productoMax)
    