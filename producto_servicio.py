# productos_servicio.py
from producto_dao import ProductoDAO
from modelo import Producto

class ProductoServicio:

    @staticmethod
    def registrar_videojuego(nombre: str, precio: float, stock: int):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del videojuego no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("La cantidad de inventario no puede ser negativa.")

        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
        ProductoDAO.registrar(nuevo_producto)

    @staticmethod
    def mostrar_inventario():
        return ProductoDAO.obtener_todos()

    @staticmethod
    def buscar_videojuego(id_producto: int):
        producto = ProductoDAO.buscar_por_id(id_producto)
        if not producto:
            raise ValueError(f"No existe ningún videojuego registrado con el ID {id_producto}.")
        return producto

    @staticmethod
    def actualizar_videojuego(id_producto: int, nombre: str, precio: float, stock: int):
        # Validar existencia previa
        ProductoServicio.buscar_videojuego(id_producto)

        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del videojuego no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("La cantidad de inventario no puede ser negativa.")

        producto_actualizado = Producto(id_producto=id_producto, nombre=nombre, precio=precio, stock=stock)
        ProductoDAO.actualizar(producto_actualizado)

    @staticmethod
    def eliminar_videojuego(id_producto: int):
        # Validar existencia previa
        ProductoServicio.buscar_videojuego(id_producto)
        ProductoDAO.eliminar(id_producto)

    @staticmethod
    def vender_unidades(id_producto: int, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")

        producto = ProductoServicio.buscar_videojuego(id_producto)

        if cantidad > producto.stock:
            raise ValueError(f"Stock insuficiente. Stock actual disponible: {producto.stock} unidades.")

        producto.stock -= cantidad
        ProductoDAO.actualizar(producto)