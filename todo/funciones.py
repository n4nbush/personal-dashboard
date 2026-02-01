from datetime import time, datetime
import sqlite3, shutil, json, os

from config import Config

DATABASE = Config.DATABASE_TODO

def init_db():
    """
    Crea la tabla 'datos' si no existe. Llamar manualmente si la DB no está creada.
    """
    os.makedirs(Config.DATABASE_FOLDER, exist_ok=True)

    db = sqlite3.connect(DATABASE)
    try:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TODO (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FECHA TEXT,
                TAREA TEXT,
                CATEGORIA TEXT,
                ESTADO BOOL
                )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CATEGORIAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                CATEGORIA TEXT
                )
        """)
        db.commit()
    finally:
        db.close()

def get_db():
    """
    Obtiene (o crea) una conexión a la base de datos por contexto de petición.
    No se comparte la conexión entre hilos.
    """
    if 'db' not in g:
        # puedes añadir detect_types o timeout si lo necesitas
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        # opcional: filas como dict
        g.db.row_factory = sqlite3.Row
    return g.db

def cargar_db(datos):
    conn = sqlite3.connect(DATABASE)
    try:
        conn.executemany(
            """INSERT INTO TODO 
               (FECHA, TAREA, CATEGORIA, ESTADO) 
               VALUES (?, ?, ?, ?)""",datos
        )
        conn.commit()
    finally:
        conn. close()

def obtener_datos(tabla):
    import sqlite3
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {tabla}")
    datos = cursor.fetchall()
    
    conn.close()
    return datos

def borrar_tabla(tabla):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Sentencia SQL para borrar la tabla 'usuarios'
    # La cláusula IF EXISTS es opcional, evita errores si la tabla no existe
    cursor.execute(f'DROP TABLE IF EXISTS "{tabla}"')
    # Confirmar los cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()
    print(f'Tabla{tabla}eliminada exitosamente')

def borrar_id(id):
    conn = sqlite3.connect(DATABASE)
    try:
            
            query = f"DELETE FROM TODO WHERE id = {id} ;" 
            conn.execute(query)
            conn.commit()
    finally:
            conn. close()

def toggle_estado(id_tarea):
    conn = sqlite3.connect(DATABASE)
    try:
        conn.execute(
            "UPDATE TODO SET ESTADO = NOT ESTADO WHERE ID = ?",
            (id_tarea,)
        )
        conn.commit()
    finally:
        conn.close()
