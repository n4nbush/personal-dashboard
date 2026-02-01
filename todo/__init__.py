from flask import Blueprint


todo_bp = Blueprint(
    'todo',
    __name__,
    template_folder='../todo/templates',
    static_folder='../todo/static'

)



from todo import routes