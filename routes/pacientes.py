from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Paciente
from schemas import PacienteSchema
from marshmallow import ValidationError

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/', methods=['GET'])
@jwt_required()
def get_pacientes():
    pacientes = Paciente.query.all()
    return jsonify(PacienteSchema(many=True).dump(pacientes))

@pacientes_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    return jsonify(PacienteSchema().dump(paciente))

@pacientes_bp.route('/', methods=['POST'])
def create_paciente():
    schema = PacienteSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    paciente = Paciente(**data)
    db.session.add(paciente)
    db.session.commit()
    
    return jsonify(schema.dump(paciente)), 201

@pacientes_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    schema = PacienteSchema()
    
    try:
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    for key, value in data.items():
        setattr(paciente, key, value)
    
    db.session.commit()
    return jsonify(schema.dump(paciente))

@pacientes_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return '', 204