# base_datos.py
import sqlite3

DB_NAME = "inventario_videojuegos.db"

def obtener_conexion():
    """Establece y retorna una conexión a la base de datos SQLite."""
    conexion = sqlite3.connect(DB_NAME)
    return conexion

def inicializar_base_datos():
    """Crea la tabla de productos si aún no existe en la base de datos."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()