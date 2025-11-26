#Sistema de Inventario

import csv


#Definir Variables (Junior)

codigo = 0
seleccion = 0
lista_productos = []
lista_historial = []

#Definir Funciones (Senior)
    #Diseniar Interfaz con prints (Junior)

def registrar_producto():
    print("Ingresar código del producto")

    while True:
        try:
            codigo = int(input("\n"))
        except ValueError:
            print("El código debe ser un número entero. Intente de nuevo.")
            continue

        codigo_registrado = set()
        for p in lista_productos:
            try:
                codigo_registrado.add(int(p[1]))
            except Exception:
                pass

        try:
            with open("inventario.csv", "r", newline="") as archivo:
                reader = csv.reader(archivo)
                for fila in reader:
                    if not fila:
                        continue
                    if fila[0].lower() == "nombre":
                        continue
                    if len(fila) > 1:
                        try:
                            codigo_registrado.add(int(fila[1]))
                        except Exception:
                            pass
        except FileNotFoundError:
            pass

        if codigo in codigo_registrado:
            print("Ese código ya está registrado. Ingrese otro.")
            continue
        else:
            break

    print("Ingresar nombre del producto")
    nombre = input("\n")

    print("Ingresar el precio del producto")
    while True:
        try:
            precio = int(input(""))
            if precio > 0:
                break
            else:
                print("Ese precio no es válido. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número entero.")

    print("Ingresar la marca del producto")
    marca = input("")

    print("Ingresar fecha de importación del producto")
    while True:
        try:
            dia = int(input("Día (00): "))
            mes = int(input("Mes (00): "))
            anio = int(input("Año (0000): "))
            fecha = f"({dia:02d}/{mes:02d}/{anio})"
            break
        except ValueError:
            print("La fecha debe ser ingresada con números. Intente de nuevo.")

    print("Ingresar daños del producto")
    danios = input("")

    print("Ingresar lugar de almacenamiento del producto")
    almacenamiento = input("")

    print("Ingresar cantidad en existencia del producto")
    while True:
        try:
            cantidad = int(input(""))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    producto = (nombre, codigo, precio, marca, fecha, danios, almacenamiento, cantidad)
    lista_productos.append(producto)

    with open("inventario.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(producto)

    registro_historial = (
        "Usuario:", str(nombre_usuario),
        "Movimiento: Registrar Producto",
        "Codigo del Producto:", codigo,
        "Fecha:", fecha_registro
    )

    lista_historial.append(registro_historial)

    with open("historial.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(registro_historial)

    print("Producto registrado")
    menu()

def registrar_venta():
    print("\n--- Registro De Venta ---")

    codigo_buscar = input("Ingrese el código del producto vendido:\n").strip()
    encontrado = False

    try:
        with open("inventario.csv", "r") as archivo:
            reader = csv.reader(archivo)
            datos = list(reader)
    except FileNotFoundError:
        print("No existe inventario registrado.\n")
        return menu()

    if len(datos) == 0:
        print("No hay productos registrados.\n")
        return menu()

    inicio = 1 if datos[0] and datos[0][0].lower() == "nombre" else 0

    for i in range(inicio, len(datos)):
        fila = datos[i]

        if not fila or len(fila) < 8:
            continue

        nombre = fila[0].strip()
        codigo = fila[1].strip()
        cantidad_actual = int(fila[7])

        if codigo_buscar == codigo:
            encontrado = True
            print(f"\nProducto encontrado: {nombre}")

            try:
                cantidad_vender = int(input("Ingrese cantidad vendida:\n"))
            except ValueError:
                print("La cantidad debe ser un número entero.")
                return menu()

            if cantidad_vender <= 0:
                print("La cantidad debe ser mayor a 0.")
                return menu()

            if cantidad_vender > cantidad_actual:
                print("No hay suficiente inventario para esta venta.")
                return menu()

            nueva_cantidad = cantidad_actual - cantidad_vender
            datos[i][7] = str(nueva_cantidad)

            with open("inventario.csv", "w", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerows(datos)

            print("\nVenta registrada con éxito.")
            print(f"Fecha de venta: {fecha_registro}")
            print(f"Cantidad restante del producto: {nueva_cantidad}")

            registro_historial = (
                "Usuario:", str(nombre_usuario),
                "Movimiento: Registrar Venta",
                "Codigo de Producto:", codigo,
                "Fecha:", fecha_registro
            )

            with open("historial.csv", "a", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(registro_historial)

            return menu()

    if not encontrado:
        print("No se encontró un producto con ese código.")
        return menu()


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

def mostrar_historial():

    print("Historial de movimientos\n")

    try:
        with open("historial.csv", "r") as archivo:
            reader = csv.reader(archivo)
            datos = list(reader)

            if len(datos) == 0:
                print("No hay movimientos registrados.\n")
                return menu()

            for linea in datos:
                for palabra in linea:
                    print(palabra, end=" ")
            

                print("\n---------------------------------------")

            return menu()

    except FileNotFoundError:
        print("No existe el archivo historial.csv\n")

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
          mostrar_historial()
     elif seleccion == 5:
           salir()
     else:
             print("Opcion Invalida")
             menu()

menu()