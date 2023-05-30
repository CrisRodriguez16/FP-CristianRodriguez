import random # SE IMPORTA LA LIBRERIA RANDOM PARA SACAR LOS GOLES DE FORMA ALEATORIA DE LOCAL Y VISITANTE

# lista equipo local
lista_Equipo_local = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico ",
                      " Alianza Petrolera ", " Atlético Nacional ", " Atlético Junior ", 
                      " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", 
                      " La Equidad ", " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", 
                      " Deportivo Pereira ", " Atlético Huila ", " Deportivo Cali ", " Unión Magdalena ",
                      " Atlético Bucaramanga ", " Once Caldas "]

# lista equpo visitante
lista_Equipo_Visitante = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico ",
                      " Alianza Petrolera ", " Atlético Nacional ", " Atlético Junior ", 
                      " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", 
                      " La Equidad ", " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", 
                      " Deportivo Pereira ", " Atlético Huila ", " Deportivo Cali ", " Unión Magdalena ",
                      " Atlético Bucaramanga ", " Once Caldas "]

# Calcular la cantidad de partidos por equipo
partidos_por_equipo = len(lista_Equipo_local) - 1
cantidad_partidos = partidos_por_equipo * len(lista_Equipo_local) // 2

# Mostrar el resultado
print(f"Cada equipo juega {partidos_por_equipo} partidos.") 

#  lista de goles equipo local usando un random de 0 a 5
lista_Goles_Equipo_local = [random.randint(0, 5) for equipo in lista_Equipo_local]

# Accediendo a los datos
for i, equipoLocal in enumerate(lista_Equipo_local): # SE REALIZA UN FOR PARA MOSTRAR LOS GOLES POR EQUIPOS
    golesEquipoLocal = lista_Goles_Equipo_local[i] # Se obtiene la información de los goles para el equipo
    print(f"Goles de equipo local {equipoLocal}: {golesEquipoLocal}") # SE IMPRIME LOS GOLES POR EQUIPO


#  lista de goles equipo visitante usando un random de 0 a 5
lista_Goles_Equipo_Visitante = [random.randint(0, 5) for equipo in lista_Equipo_Visitante]

# Accediendo a los datos
for i, equipoVisitante in enumerate(lista_Equipo_Visitante): # SE REALIZA UN FOR PARA MOSTRAR LOS GOLES POR EQUIPOS VISITANTES
    golesEquipoVisitante = lista_Goles_Equipo_Visitante[i] # Se obtiene la información de los goles para el equipo visitante
    print(f"Goles de equipo visitante {equipoVisitante}: {golesEquipoVisitante}") # SE IMPRIME LOS GOLES POR EQUIPO


# Inicializar la variable total_goles
total_goles = 0

# Bucle for para sumar los goles de todos los partidos
for goles_local, goles_visitante in zip(lista_Goles_Equipo_local, lista_Goles_Equipo_Visitante):
    total_goles += goles_local + goles_visitante

# Imprimir el resultado
print(f"Total de goles en todos los partidos: {total_goles}")

# Inicializar el diccionario para almacenar la cantidad de goles de cada equipo
goles_por_equipo = {equipo: 0 for equipo in lista_Equipo_local}

# Bucle for para sumar los goles de cada equipo en todos los partidos
for goles_local, goles_visitante, equipo_local, equipo_visitante in zip(lista_Goles_Equipo_local, lista_Goles_Equipo_Visitante, lista_Equipo_local, lista_Equipo_Visitante):
    goles_por_equipo[equipo_local] += goles_local
    goles_por_equipo[equipo_visitante] += goles_visitante

# Encontrar el equipo con la cantidad de goles máxima
equipo_con_mas_goles = max(goles_por_equipo, key=goles_por_equipo.get)

# Imprimir el resultado
print(f"El equipo que hizo más goles fue {equipo_con_mas_goles} con {goles_por_equipo[equipo_con_mas_goles]} goles.")

# Inicializar el diccionario para almacenar los puntos de cada equipo
puntos_por_equipo = {equipo: 0 for equipo in lista_Equipo_local}

# Bucle for para sumar los puntos de cada equipo en todos los partidos
for goles_local, goles_visitante, equipo_local, equipo_visitante in zip(lista_Goles_Equipo_local, lista_Goles_Equipo_Visitante, lista_Equipo_local, lista_Equipo_Visitante):
    if goles_local > goles_visitante:
        puntos_por_equipo[equipo_local] += 3
    elif goles_local < goles_visitante:
        puntos_por_equipo[equipo_visitante] += 3
    else:
        puntos_por_equipo[equipo_local] += 1
        puntos_por_equipo[equipo_visitante] += 1

# Crear una lista de tuplas (equipo, puntos) y ordenarla de mayor a menor por puntos
tabla_posiciones = sorted(puntos_por_equipo.items(), key=lambda x: x[1], reverse=True)

# Imprimir la tabla de posiciones
print("Tabla de posiciones:")
print("--------------------")
for i, (equipo, puntos) in enumerate(tabla_posiciones):
    print(f"{i+1}. {equipo}: {puntos} puntos")
