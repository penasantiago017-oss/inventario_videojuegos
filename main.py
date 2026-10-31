# main.py
from base_datos import inicializar_base_datos
from producto_servicio import ProductoServicio

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def solicitar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

def mostrar_menu():
    print("\n========================================")
    print("    SISTEMA DE INVENTARIO - VIDEOJUEGOS  ")
    print("========================================")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego por ID")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")
    print("========================================")

def ejecutar_app():
    inicializar_base_datos()

    while True:
        mostrar_menu()
        opcion = solicitar_entero("Seleccione una opción (1-7): ")

        try:
            if opcion == 1:
                print("\n--- Registrar Videojuego ---")
                nombre = input("Ingrese el nombre: ")
                precio = solicitar_flotante("Ingrese el precio: ")
                stock = solicitar_entero("Ingrese el stock inicial: ")
                
                ProductoServicio.registrar_videojuego(nombre, precio, stock)
                print("\n¡Producto guardado correctamente!")

            elif opcion == 2:
                print("\n--- Inventario de Videojuegos ---")
                productos = ProductoServicio.mostrar_inventario()
                if not productos:
                    print("El inventario está vacío.")
                else:
                    for p in productos:
                        print(p)

            elif opcion == 3:
                print("\n--- Buscar Videojuego ---")
                id_prod = solicitar_entero("Ingrese el ID del videojuego a buscar: ")
                producto = ProductoServicio.buscar_videojuego(id_prod)
                print("\nProducto encontrado:")
                print(producto)

            elif opcion == 4:
                print("\n--- Actualizar Videojuego ---")
                id_prod = solicitar_entero("Ingrese el ID del videojuego a actualizar: ")
                # Validar existencia antes de pedir los nuevos datos
                ProductoServicio.buscar_videojuego(id_prod)
                
                nombre = input("Ingrese el nuevo nombre: ")
                precio = solicitar_flotante("Ingrese el nuevo precio: ")
                stock = solicitar_entero("Ingrese el nuevo stock: ")
                
                ProductoServicio.actualizar_videojuego(id_prod, nombre, precio, stock)
                print("\n¡Producto actualizado correctamente!")

            elif opcion == 5:
                print("\n--- Eliminar Videojuego ---")
                id_prod = solicitar_entero("Ingrese el ID del videojuego a eliminar: ")
                ProductoServicio.eliminar_videojuego(id_prod)
                print("\n¡Producto eliminado correctamente del inventario!")

            elif opcion == 6:
                print("\n--- Vender Unidades ---")
                id_prod = solicitar_entero("Ingrese el ID del videojuego: ")
                cantidad = solicitar_entero("Ingrese la cantidad a vender: ")
                
                ProductoServicio.vender_unidades(id_prod, cantidad)
                print("\n¡Venta registrada con éxito! Stock actualizado.")

            elif opcion == 7:
                print("\nSaliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Por favor, elija un número entre 1 y 7.")

        except ValueError as e:
            print(f"\n[Error de validación]: {e}")
        except Exception as e:
            print(f"\n[Error inesperado]: {e}")

if __name__ == "__main__":
    ejecutar_app()