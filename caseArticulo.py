producto = []
precio = []
unidadesExistentes = []
codigo = []
descripcionProducto = []
estadoProducto = []
#i = 0 #Esta es la variable de control para el ciclo for (case 2)    
opcion = 0

while True:
    print("Bienvenido al sistema de inventario de productos")
    print("---------MENU PRINCIPAL---------")
    print("1. Registrar producto")
    print("2. Ver información del inventario")
    print("3. Borrar información del inventario")
    print ("4. Modificar información del inventario")
    print("5. Salir")
    print("---------------------------------")
    opcion = int(input("Selecciona una opción: "))

    match opcion:#Aquí inicia el match, que es una validación de caso
    
        case 1:
            producto.append(input("Ingresa el nombre de el producto: "))
            precio.append(input("Ingresa el precio del producto: "))
            unidadesExistentes.append(int(input("Ingresa el número de unidades existentes: ")))
            codigo.append(input("Ingresa el código del producto: "))
            descripcionProducto.append(input("Ingresa la descripción del producto: "))
            estadoProducto.append(input("Ingresa el estado del producto: "))
            print("Producto registrado con éxito, con el ID: " + str(len(producto) -1))
        
        case 2:
            print("Lista de productos registrados:")
            for i in range(len(producto)):
                print("Id:-", i," con el nombre", producto[i]," con el precio", precio[i]," con las unidades existentes", unidadesExistentes[i]," con el código", codigo[i]," con la descripción", descripcionProducto[i]," con el estado", estadoProducto[i])
                #i +=1

        case 3:
            index = int(input("Ingresa el índice del producto a borrar (empezando desde 0): "))

        case 4:
            print("lista de productos registrados:")

        case 5:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción no válida")
        
