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
    print("Mostrar Inventario")
    for i in range(len(lista_productos)):
         print(lista_productos[i],sep="\t")
    menu()

def salir():
    print("Gracias, vuelva pronto!")

    #Diseniar interfaz de inventario con print (Mostrar Codigo/Nombre/Precio/etc.)(Mid)

#Mensaje de Bienvenida y mostrar Opciones (Mid)
#Registrar Fecha en formato (dd/mm/aaaa) (Mid)
#Registrar nombre del usuario (Junior)

def menu():
     seleccion = 0
     print("Opciones (1-4)")
     seleccion = int(input("\n"))
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