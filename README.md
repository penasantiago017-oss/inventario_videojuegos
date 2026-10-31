# Video Game Inventory System (CRUD + SQLite + DAO Pattern)

Aplicación de consola desarrollada en Python para la administración de inventario de videojuegos. El sistema cumple con la separación estricta de responsabilidades mediante el patrón **DAO (Data Access Object)** y persistencia local en **SQLite**.

## 📁 Estructura del Proyecto
- `modelo.py`: Contiene la clase `Producto`.
- `base_datos.py`: Gestiona la conexión y la creación inicial de la base de datos SQLite.
- `producto_dao.py`: Implementa las consultas y operaciones SQL directas.
- `producto_servicio.py`: Centraliza las reglas de negocio y validaciones obligatorias.
- `main.py`: Maneja el menú interactivo por consola y el flujo de la aplicación.

## ⚙️ Instrucciones de Ejecución
1. Asegúrate de tener instalado Python.
2. Ejecuta el programa principal en la terminal:
   ```bash
   python main.py

   ## 📸 Evidence of Operation

### 1. Operación Exitosa (Registro y Listado)
![Operación Exitosa](Operación%20Exitosas.jpeg)

### 2. Operación Rechazada (Validación de Stock)
![Operación Rechazada](Operación%20Rechazada.jpeg)