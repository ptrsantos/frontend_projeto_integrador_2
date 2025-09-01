from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Prontuario
from schemas import ProntuarioSchema
from marshmallow import ValidationError

prontuarios_bp = Blueprint('prontuarios', __name__)

@prontuarios_bp.route('/', methods=['GET'])
@jwt_required()
def get_prontuarios():
    prontuarios = Prontuario.query.order_by(Prontuario.data_criacao.desc()).all()
    return jsonify(ProntuarioSchema(many=True).dump(prontuarios))

@prontuarios_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_prontuario(id):
    prontuario = Prontuario.query.get_or_404(id)
    return jsonify(ProntuarioSchema().dump(prontuario))

@prontuarios_bp.route('/paciente/<int:paciente_id>', methods=['GET'])
@jwt_required()
def get_prontuarios_paciente(paciente_id):
    prontuarios = Prontuario.query.filter_by(id_paciente=paciente_id).order_by(Prontuario.data_criacao.desc()).all()
    return jsonify(ProntuarioSchema(many=True).dump(prontuarios))

@prontuarios_bp.route('/', methods=['POST'])
@jwt_required()
def create_prontuario():
    schema = ProntuarioSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    # Usar o profissional logado
    data['id_profissional'] = get_jwt_identity()
    
    prontuario = Prontuario(**data)
    db.session.add(prontuario)
    db.session.commit()
    
    return jsonify(schema.dump(prontuario)), 201

@prontuarios_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_prontuario(id):
    prontuario = Prontuario.query.get_or_404(id)
    schema = ProntuarioSchema()
    
    try:
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    for key, value in data.items():
        if key != 'id_profissional':  # Não permitir alterar o profissional
            setattr(prontuario, key, value)
    
    db.session.commit()
    return jsonify(schema.dump(prontuario))

@prontuarios_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_prontuario(id):
    prontuario = Prontuario.query.get_or_404(id)
    db.session.delete(prontuario)
    db.session.commit()
    return '', 204