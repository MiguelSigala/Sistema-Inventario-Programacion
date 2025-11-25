#Sistema de Inventario

import csv

#Definir Variables (Junior)

codigo = 0
seleccion = 0
lista_productos = []

#Definir Funciones (Senior)
    #Diseniar Interfaz con prints (Junior)

def registrar_producto():

    print("\n" + "="*60)
    print("         SISTEMA DE INVENTARIO - REGISTRO DE PRODUCTO")
    print("="*60)

    print("\n[1] Datos de identificación")
    print("-"*60)

    while True:
        try:
            codigo = int(input("   ➤ Ingresa el CÓDIGO numérico del producto: "))
        except ValueError:
            print("   ⚠ El código debe ser un número entero. Intenta de nuevo.")
            continue

        
        codigo_repetido = False
        for prod in lista_productos:
            if codigo == prod[1]:      
                codigo_repetido = True
                break

        if codigo_repetido:
            print("   ❌ Ese código YA está registrado. Escribe uno diferente.")
        else:
            print("   ✅ Código disponible.")
            break

    
    while True:
        nombre = input("\n   ➤ Ingresa el NOMBRE del producto: ").strip().title()
        if nombre == "":
            print("   ⚠ El nombre no puede estar vacío.")
            continue

        nombre_repetido = False
        for prod in lista_productos:
            if nombre.lower() == prod[0].lower():   
                nombre_repetido = True
                break

        if nombre_repetido:
            print("   ❌ Ese nombre YA está registrado. Usa uno diferente.")
        else:
            print("   ✅ Nombre disponible.")
            break

    
    print("\n[2] Datos económicos")
    print("-"*60)

    while True:
        try:
            precio = float(input("   ➤ Ingresa el PRECIO del producto: "))
            if precio <= 0:
                print("   ⚠ El precio debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("   ⚠ Ingresa un valor numérico válido para el precio.")

    
    print("\n[3] Información general")
    print("-"*60)

    marca = input("   ➤ Ingresa la MARCA del producto: ").strip().title()
    fecha = input("   ➤ Ingresa la FECHA de importación (dd/mm/aaaa): ").strip()
    danios = input("   ➤ Ingresa los DAÑOS del producto (si no tiene, escribe 'Ninguno'): ").strip()
    almacenamiento = input("   ➤ Ingresa el LUGAR de ALMACENAMIENTO: ").strip()

    while True:
        try:
            cantidad = int(input("   ➤ Ingresa la CANTIDAD en existencia: "))
            if cantidad < 0:
                print("   ⚠ La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("   ⚠ La cantidad debe ser un número entero.")

    
    producto = (nombre, codigo, precio, marca, fecha, danios, almacenamiento, cantidad)
    lista_productos.append(producto)

    with open("inventario.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(producto)

    print("\n" + "-"*60)
    print(f" Producto '{nombre}' registrado correctamente en el inventario.")
    print("-"*60 + "\n")

    input("Presiona ENTER para volver al menú...")
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
    print("¡Gracias, vuelva pronto!")

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
     print("- 2. Registrar venta")
     print("- 3. Mostrar inventario")
     print("- 4. Mostrar historial")
     print("- 5. Salir del sistema")
     print("========================\n")
     seleccion = 0
     seleccion = int(input("Selecciona una opcion (1-5): "))
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