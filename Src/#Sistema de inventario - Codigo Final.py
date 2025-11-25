#Sistema de Inventario

import csv

#Definir Variables (Junior)

codigo = 0
seleccion = 0
lista_productos = []

#Definir Funciones (Senior)
    #Diseniar Interfaz con prints (Junior)

def registrar_producto():
    print("Ingresar codigo del producto")
    codigo = int(input("\n"))
    for i in lista_productos:
            if codigo == i[0]:
                print("\nese codigo ya esta registrado")
                registrar_producto()
    print("Ingresar Nombre del producto")
    nombre = (input("\n"))
    for i in lista_productos:
            if nombre == i[0]:
                print("\nese codigo ya esta registrado")
                registrar_producto()
    print("Ingresar el Precio del producto")
    precio = int(input(""))
    while precio <= 0:
         print("Ese precio no es valido, intente de nuevo")
         precio = int(input(""))
    print("Ingresar la Marca del producto")
    marca = (input(""))
    print("Ingresar la Fecha de importacion del producto")
    fecha = (input(""))
    print("Ingresar danios del producto")
    danios = (input(""))
    print("Ingresar lugar del almacenamiento producto")
    almacenamiento = (input(""))
    print("Ingresar cantidad en existencia del producto")
    cantidad = (input(""))
    producto = (nombre,codigo,precio,marca,fecha,danios,almacenamiento,cantidad)
    lista_productos.append(producto)
    with open("inventario.csv", "a") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(producto)
    print("Producto Registrado")
    menu()


#Definir funcion de registrar venta(Mid)

def registrar_venta():
    print("\n--- Registro De Venta ---")

    codigo_buscar = int(input("Ingrese el código del producto vendido:\n"))
    encontrado = False
    for i in range(len(lista_productos)):
        producto = lista_productos[i]
        nombre = producto[0]
        codigo = producto[1]
        cantidad_actual = int(producto[7])

        if codigo_buscar == codigo:
            encontrado = True
            print(f"Producto encontrado: {nombre}")
            cantidad_vender = int(input("Ingrese cantidad vendida:\n"))
            
            if cantidad_vender <= 0:
                print("La cantidad debe ser mayor a 0.")
                menu()
                return

            if cantidad_vender > cantidad_actual:
                print("No hay suficiente inventario para esta venta.")
                menu()
                return

            nueva_cantidad = cantidad_actual - cantidad_vender

            lista_productos[i] = (
                producto[0], producto[1], producto[2], producto[3],
                producto[4], producto[5], producto[6], str(nueva_cantidad)
            )

            with open("inventario.csv", "w", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["Nombre", "Código", "Precio", "Marca", "Fecha", "Daños", "Almacenamiento", "Cantidad"])
                writer.writerows(lista_productos)

            print("\nVenta registrada con éxito.")
            print(f"Fecha de venta: {fecha_registro}")
            print(f"Cantidad restante del producto: {nueva_cantidad}")

            menu()
            return

    if not encontrado:
        print("No se encontró un producto con ese código.")
        menu()

import csv

def mostrar_inventario():
    print("\n=============== INVENTARIO ===============\n")

    try:
        with open("inventario.csv", "r") as archivo:
            reader = csv.reader(archivo)
            datos = list(reader)

            if len(datos) <= 1:
                print("No hay productos registrados.\n")
                return menu()

            start = 1 if datos[0][0].lower() == "nombre" else 0

            for producto in datos[start:]:

                if len(producto) < 8:
                    continue

                print("Codigo: ", producto[1])
                print("Nombre: ", producto[0])
                print("Precio: ", producto[2])
                print("Marca: ", producto[3])
                print("Fecha de importacion: ", producto[4])
                print("Daños: ", producto[5])
                print("Almacenamiento: ", producto[6])
                print("Cantidad: ", producto[7])
                print("\n==========================================")

    except FileNotFoundError:
        print("No existe el archivo inventario.csv\n")

    return menu()

def salir():
    print("Gracias, vuelva pronto!")

#Diseniar interfaz de inventario con print (Mostrar Codigo/Nombre/Precio/etc.)(Mid)

#Mensaje de Bienvenida y mostrar Opciones (Mid)

print("=======================================================")
print("       SISTEMA DE INVENTARIO - TIENDA AUTOMOTRIZ")
print("=======================================================\n")
#Registrar Fecha en formato (dd/mm/aaaa) (Mid)

print("Ingresa la fecha del día de hoy: \n")

###Definir condicional si el anio es invalido (si es mayor a 2025 y si es menor a 2000)(Mid)

dia = int(input("Día (00): "))
mes = int(input("Mes (00): "))
anio = int(input("Año (0000): "))
fecha_registro = (dia, mes, anio)
print("Fecha registrada: ", fecha_registro)

#Registrar nombre del usuario (Junior)
nombre_usuario = input(str())
print(f"Bienvenido/a {nombre_usuario}. Fecha registrada: {fecha_registro}\n")

##Corregir menu (Jr)
def menu():
     print("========= MENU =========\n")
     print("- 1. Registrar producto")
     print("- 1. Registrar venta")
     print("- 1. Mostrar inventarioo")
     print("- 1. Salir del sistema")
     seleccion = 0
     print("Opciones (1-4)")
     seleccion = int(input("Selecciona una opcion (1-4): \n"))
     if seleccion == 1:
        print("")
        registrar_producto()
     elif seleccion == 2:
               print("")
               registrar_venta()
     elif seleccion == 3:
              print("")
              mostrar_inventario()
     elif seleccion == 4:
           salir()
     else:
             print("Opcion Invalida")
             menu()
     
menu()