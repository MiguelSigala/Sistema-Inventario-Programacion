#Sistema de Inventario

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
    print("Producto Registrado")
    menu()


def registrar_venta():
    print("Registrar Venta")

    #Definir funcion de registrar venta(Mid)
    
    menu()

def mostrar_inventario():
    print("\n=============== INVENTARIO ===============")
    if len(lista_productos) == 0:
          print("No hay productos registrados. \n")
          return menu()
    
    for producto in lista_productos:
          print("Codigo: ", producto[1])
          print("Nombre: ", producto[0])
          print("Precio: ", producto[2])
          print("Marca: ", producto[3])
          print("Fecha de importancion: ", producto[4])
          print("Daños: ", producto[5])
          print("Almacenamiento: ", producto[6])
          print("Cantidad: ", producto[7])
          print("\n==========================================")
          
    menu()

def salir():
    print("Gracias, vuelva pronto!")

    #Diseniar interfaz de inventario con print (Mostrar Codigo/Nombre/Precio/etc.)(Mid)

#Mensaje de Bienvenida y mostrar Opciones (Mid)

print("=======================================================")
print("       SISTEMA DE INVENTARIO - TIENDA AUTOMOTRIZ")
print("=======================================================\n")
#Registrar Fecha en formato (dd/mm/aaaa) (Mid)

#Registrar nombre del usuario (Junior)

print(f"Bienvenido/a {nombre_usuario}. Fecha registrada: {fecha_hoy}\n")

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