from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from auth import auth_bp
from routes.pacientes import pacientes_bp
from routes.agendamentos import agendamentos_bp
from routes.prontuarios import prontuarios_bp
from routes.profissionais import profissionais_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensões
    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app)
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # Registrar blueprints
    app.register_blueprint(pacientes_bp, url_prefix='/api/pacientes')
    app.register_blueprint(agendamentos_bp, url_prefix='/api/agendamentos')
    app.register_blueprint(prontuarios_bp, url_prefix='/api/prontuarios')
    app.register_blueprint(profissionais_bp, url_prefix='/api/profissionais')
    
    # Handler para token expirado
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({'error': 'Token expirado'}), 401
    
    # Handler para token inválido
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'error': 'Token inválido'}), 401
    
    # Handler para token ausente
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'error': 'Token de acesso necessário'}), 401
    
    # Rota de health check
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'OK', 'message': 'API Clínica Mentalize funcionando'})
    
    # Não criar tabelas automaticamente - usar banco existente
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)