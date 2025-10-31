#Sistema de inventario - Pseudocodigo

# =====================================
# SISTEMA DE INVENTARIO - TIENDA AUTOMOTRIZ
# =====================================

# Paso 1: Preguntar cuántos productos se registrarán
num_productos = int(input("¿Cuántos productos se registrarán? "))

# Paso 2: Variables acumuladoras
inventario = ""
total_productos = 0
total_valor_inventario = 0
producto_menor_stock = None
producto_mayor_stock = None
menor_stock = None
mayor_stock = None

# Paso 3: Ciclo para registrar cada producto
for i in range(num_productos):
    print(f"\n--- Registro del producto #{i+1} ---")

    # Entradas del usuario
    nombre = input("Nombre del producto: ")
    codigo = input("Código del producto: ")
    marca = input("Marca: ")
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad en existencia: "))
    lugar = input("Lugar de almacenamiento: ")

    # Validaciones
    if precio <= 0:
        print("Error: el precio debe ser mayor a 0.")
        continue

    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
        continue

    # Calcular valor total del producto (precio * cantidad)
    valor_total = precio * cantidad

    # Acumular totales
    total_valor_inventario += valor_total
    total_productos += cantidad

    # Guardar en resumen
    inventario += (f"Nombre: {nombre} | Código: {codigo} | Marca: {marca} | "
                   f"Precio: ${precio:.2f} | Cantidad: {cantidad} | "
                   f"Lugar: {lugar} | Valor total: ${valor_total:.2f}\n")

    # Identificar producto con menor y mayor stock
    if menor_stock is None or cantidad < menor_stock:
        menor_stock = cantidad
        producto_menor_stock = nombre

    if mayor_stock is None or cantidad > mayor_stock:
        mayor_stock = cantidad
        producto_mayor_stock = nombre

# Paso 4: Imprimir el reporte final
print("\n=====================================")
print("REPORTE FINAL - INVENTARIO AUTOMOTRIZ")
print("=====================================")
print(f"Total de productos registrados: {num_productos}\n")

print("Resumen de productos:")
print(inventario)

print("-------------------------------------")
print(f"Total de piezas en inventario: {total_productos}")
print(f"Valor total del inventario: ${total_valor_inventario:.2f}")
print(f"Producto con menor stock: {producto_menor_stock} ({menor_stock} unidades)")
print(f"Producto con mayor stock: {producto_mayor_stock} ({mayor_stock} unidades)")
print("=====================================")