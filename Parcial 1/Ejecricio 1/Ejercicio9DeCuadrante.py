coordenada_x = int(input("Ingrese la coordenada en el eje X: "))
coordenada_y = int(input("Ingrese la coordenada en el eje y: "))

if coordenada_x > 0 and coordenada_y > 0:
    print("El punto esta en el primer cuadrante.")
elif coordenada_x < 0 and coordenada_y > 0:
    print("El punto esta en el segundo cuadrante.")
elif coordenada_x < 0 and coordenada_y < 0:
    print("El punto esta en el tercer cuadrante.")
elif coordenada_x > 0 and coordenada_y < 0:
    print("El punto esta en el cuarto cuadrante.")
else:
    print("El esta encuentra en el origen.")