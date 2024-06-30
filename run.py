from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de la apliacion con Flask
app = Flask(__name__)



init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#registrar una ruta asociada a una vista
app.route('/',methods=['GET'])(index)
app.route('/api/vinos/',methods=['GET'])(get_all_vinos)
app.route('/api/vinos/',methods=['POST'])(create_vino)
app.route('/api/vinos/<int:vino_id>', methods=['GET'])(get_vino)
app.route('/api/vinos/<int:vino_id>', methods=['PUT'])(update_vino)
app.route('/api/vinos/<int:vino_id>', methods=['DELETE'])(delete_vino)

if __name__ == '__main__':
    #levanta servidor de desarrollo flask
    app.run(debug=True)




