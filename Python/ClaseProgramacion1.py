nombres = []
edades = []

for x in range(2):
    nom = input("Ingrese el nombre del estudiante: ")
    #eds = int(input("Ingrese la edad de {}: ".format(nom)))
    eds = int(input("Ingrese la edad: "))
    nombres.append(nom)
    edades.append(eds)

print("\nEstas personas son mayores de edad:")
for x in range(2):
    if edades [x] >= 18:
        print(nombres[x])


