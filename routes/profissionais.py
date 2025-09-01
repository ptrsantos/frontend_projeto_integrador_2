from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Profissional
from schemas import ProfissionalSchema
from marshmallow import ValidationError
import bcrypt

profissionais_bp = Blueprint('profissionais', __name__)

@profissionais_bp.route('/', methods=['GET'])
@jwt_required()
def get_profissionais():
    profissionais = Profissional.query.all()
    return jsonify(ProfissionalSchema(many=True).dump(profissionais))

@profissionais_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_profissional(id):
    profissional = Profissional.query.get_or_404(id)
    return jsonify(ProfissionalSchema().dump(profissional))

@profissionais_bp.route('/', methods=['POST'])
@jwt_required()
def create_profissional():
    schema = ProfissionalSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    # Hash da senha
    if 'senha' in request.json:
        senha_hash = bcrypt.hashpw(request.json['senha'].encode('utf-8'), bcrypt.gensalt())
        data['senha'] = senha_hash.decode('utf-8')
    
    profissional = Profissional(**data)
    db.session.add(profissional)
    db.session.commit()
    
    return jsonify(schema.dump(profissional)), 201

@profissionais_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_profissional(id):
    profissional = Profissional.query.get_or_404(id)
    schema = ProfissionalSchema()
    
    try:
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    # Hash da senha se fornecida
    if 'senha' in request.json:
        senha_hash = bcrypt.hashpw(request.json['senha'].encode('utf-8'), bcrypt.gensalt())
        data['senha'] = senha_hash.decode('utf-8')
    
    for key, value in data.items():
        setattr(profissional, key, value)
    
    db.session.commit()
    return jsonify(schema.dump(profissional))

@profissionais_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_profissional(id):
    profissional = Profissional.query.get_or_404(id)
    db.session.delete(profissional)
    db.session.commit()
    return '', 204