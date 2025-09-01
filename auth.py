from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Profissional
from schemas import LoginSchema, ProfissionalSchema
from marshmallow import ValidationError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    schema = LoginSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'error': 'Dados inválidos', 'messages': err.messages}), 400
    
    profissional = Profissional.query.filter_by(usuario=data['usuario']).first()
    
    if profissional and profissional.check_password(data['senha']):
        access_token = create_access_token(identity=profissional.id)
        return jsonify({
            'access_token': access_token,
            'profissional': ProfissionalSchema().dump(profissional)
        })
    
    return jsonify({'error': 'Credenciais inválidas'}), 401

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    profissional = Profissional.query.get(current_user_id)
    
    if not profissional:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    
    return jsonify(ProfissionalSchema().dump(profissional))