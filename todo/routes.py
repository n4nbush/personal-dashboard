from flask import Flask, render_template,g, request, redirect, url_for, flash, current_app
from . import todo_bp
from datetime import datetime
from . import funciones

@todo_bp.route('/')
def index():
    funciones.init_db()
    tareas = funciones.obtener_datos("TODO")
    context = {
        'tareas' : tareas
    }
    return render_template('index.html',**context)

@todo_bp.route('/agregar_tarea', methods=['POST'])
def registrar_tarea():
    try:
        now = datetime.now()
        tarea = request.form['tarea']
        estado = False
        categoria = request.form['categoria']

        fecha = now.strftime("%Y-%m-%d %H:%M:%S")

        datos = [(fecha,tarea,categoria,estado)]

        funciones.cargar_db(datos)

    except ValueError as e:
        flash('❌ El monto debe ser un número válido', 'error')
        print(f"ValueError: {e}")
    except Exception as e:
        flash(f'❌ Error: {str(e)}', 'error')
        print(f"Error general: {e}")
        
    return redirect(url_for('todo.index'))

@todo_bp.route('/borrar', methods=['POST'])
def borrar_tarea():
    try:
        id = request.form['id']

        funciones.borrar_id(id)
    except ValueError as e:
        flash('❌ El monto debe ser un número válido', 'error')
        print(f"ValueError: {e}")
    except Exception as e:
        flash(f'❌ Error: {str(e)}', 'error')
        print(f"Error general: {e}")
    return redirect(url_for('todo.index'))

@todo_bp.route('/completar', methods=['POST'])
def completar_tarea():
    try:
        id = request.form['id']

        funciones.toggle_estado(id)
    except ValueError as e:
        flash('❌ El monto debe ser un número válido', 'error')
        print(f"ValueError: {e}")
    except Exception as e:
        flash(f'❌ Error: {str(e)}', 'error')
        print(f"Error general: {e}")
    return redirect(url_for('todo.index'))