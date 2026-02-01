import os

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # base de datos
    DATABASE_FOLDER = os.path.join(BASE_DIR,'database')
    DATABASE_TODO = os.path.join(DATABASE_FOLDER,'database_todo.db')
    DATABASE_GASTOS = os.path.join(DATABASE_FOLDER,'database_gastos.db')

    

    BACKUP_FOLDER = os.path.join(BASE_DIR,'backup')
    BACKUP = os.path.join(BACKUP_FOLDER,'fecha_ultimo_backup.json')