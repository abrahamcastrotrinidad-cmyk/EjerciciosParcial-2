nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18: # el if va seguido de la condición y dos puntos
    print("Eres mayor de edad")
else: # ele else va seguido de dos puntos para decir que se hace si no se cumple la condición del if
    print("No eres mayor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")
