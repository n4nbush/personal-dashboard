from flask import Blueprint

gastos_bp = Blueprint(
    'gastos',
    __name__,
    template_folder= '../gestor_gastos/templates',
    static_folder= '../gestor_gastos/static'
)

from gestor_gastos import routes