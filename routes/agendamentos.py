from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Agendamento, Paciente
from schemas import AgendamentoSchema, PacienteSchema
from marshmallow import ValidationError
from datetime import datetime

agendamentos_bp = Blueprint('agendamentos', __name__)

@agendamentos_bp.route('/', methods=['GET'])
@jwt_required()
def get_agendamentos():
    agendamentos = Agendamento.query.order_by(Agendamento.data_agendamento, Agendamento.hora_agendamento).all()
    return jsonify(AgendamentoSchema(many=True).dump(agendamentos))

@agendamentos_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify(AgendamentoSchema().dump(agendamento))

@agendamentos_bp.route('/', methods=['POST'])
def create_agendamento():
    schema = AgendamentoSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    # Criar paciente se não existir
    if 'paciente_nome' in request.json:
        paciente = Paciente(
            nome=request.json['paciente_nome'],
            telefone=request.json.get('paciente_telefone'),
            email=request.json.get('paciente_email')
        )
        db.session.add(paciente)
        db.session.flush()
        data['id_paciente'] = paciente.id
    
    agendamento = Agendamento(**data)
    db.session.add(agendamento)
    db.session.commit()
    
    return jsonify(schema.dump(agendamento)), 201

@agendamentos_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    schema = AgendamentoSchema()
    
    try:
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    for key, value in data.items():
        setattr(agendamento, key, value)
    
    db.session.commit()
    return jsonify(schema.dump(agendamento))

@agendamentos_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    return '', 204

@agendamentos_bp.route('/hoje', methods=['GET'])
@jwt_required()
def get_agendamentos_hoje():
    hoje = datetime.now().date()
    agendamentos = Agendamento.query.filter_by(data_agendamento=hoje).order_by(Agendamento.hora_agendamento).all()
    return jsonify(AgendamentoSchema(many=True).dump(agendamentos))