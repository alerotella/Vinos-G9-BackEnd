from flask import jsonify, request
from app.models import Vino

def index():
    response = {'message':'Hola Mundo API-REST Flask 🐍'}
    return jsonify(response)

def get_all_vinos():
    vinos = Vino.get_all()
    return jsonify([vino.serialize() for vino in vinos])

def get_vino(vino_id):
    vino = Vino.get_by_id(vino_id)
    if not vino:
        return jsonify({'message': 'Recomendación not found'}), 404
    return jsonify(vino.serialize())

def create_vino():
    #obtengo los datos enviados en formato json - convierte en un diccionario python
    data = request.json
    #PROCESO DE VALIDACION 
    #if(data['title']==''):
    #    return jsonify({'message':'El campo titulo es obligatorio'}), 500    
    new_vino = Vino(None,data['nombre'],data['nombre_vino'],data['año_vino'],data['foto'])
    new_vino.save()
    response = {'message':'Recomendación creada con exito'}
    return jsonify(response) , 201

def update_vino(vino_id):
    vino = Vino.get_by_id(vino_id)
    if not vino:
        return jsonify({'message': 'Recomendación not found'}), 404
    data = request.json
    vino.nombre = data['nombre']
    vino.nombre_vino = data['nombre_vino']
    vino.año_vino = data['año_vino']
    vino.foto = data['foto']
    vino.save()
    return jsonify({'message': 'Recomendación updated successfully'})

def delete_vino(vino_id):
    vino = Vino.get_by_id(vino_id)
    if not vino:
        return jsonify({'message': 'Recomendación not found'}), 404
    vino.delete()
    return jsonify({'message': 'Recomendación deleted successfully'})

