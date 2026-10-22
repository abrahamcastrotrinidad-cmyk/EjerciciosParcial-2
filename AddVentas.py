producto = ""
precio = 0
clave = 0
codigo = 0
unidadesExistentes = 0
unidadesVentas = 0


print("El producto es", producto)
print("El precio de", producto, "es", precio)
print("La clave de", producto, "es", clave)
print("El código de", producto, "es", codigo)
print("Las unidades existentes de", producto, "son", unidadesExistentes)
print("Las unidades vendidas de", producto, "son", unidadesVentas)


producto=input("Ingrese el nombre del producto: ")
precio=int(input("Ingrese el precio del producto: "))
clave=int(input("Ingrese la clave del producto: "))
codigo=int(input("Ingrese el código del producto: "))
unidadesExistentes=int(input("Ingrese las unidades existentes del producto: "))
unidadesVentas=int(input("Ingrese las unidades vendidas del producto: "))

if unidadesVentas > unidadesExistentes:
    print("No se puede realizar la venta, no hay suficientes unidades")
else:
    print("La venta se ha realizado con éxito")

if len(producto) == 0:
    print("El nombre del producto no puede estar vacío")
else:
    print("El nombre del producto es", producto)

