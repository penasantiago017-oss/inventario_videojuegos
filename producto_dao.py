# producto_dao.py
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:

    @staticmethod
    def registrar(producto: Producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (producto.nombre, producto.precio, producto.stock)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos")
        filas = cursor.fetchall()
        conexion.close()

        productos = []
        for fila in filas:
            productos.append(Producto(id_producto=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3]))
        return productos

    @staticmethod
    def buscar_por_id(id_producto: int):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (id_producto,))
        fila = cursor.fetchone()
        conexion.close()

        if fila:
            return Producto(id_producto=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3])
        return None

    @staticmethod
    def actualizar(producto: Producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
            (producto.nombre, producto.precio, producto.stock, producto.id_producto)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_producto: int):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        conexion.close()