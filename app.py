from flask import Flask, render_template,g, request, redirect, url_for, flash
from todo.routes import todo_bp
from gestor_gastos.routes import gastos_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui-cambiar-en-produccion'

app.register_blueprint(todo_bp,url_prefix='/todo')
app.register_blueprint(gastos_bp,url_prefix='/gs')


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)