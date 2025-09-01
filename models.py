from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

db = SQLAlchemy()

class Profissional(db.Model):
    __tablename__ = 'profissionais'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    especialidade = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.senha.encode('utf-8'))

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissionais.id'))
    data_agendamento = db.Column(db.Date, nullable=False)
    hora_agendamento = db.Column(db.Time, nullable=False)
    observacoes = db.Column(db.Text)
    status = db.Column(db.Enum('agendado', 'cancelado', 'realizado'), default='agendado')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    paciente = db.relationship('Paciente', backref='agendamentos')
    profissional = db.relationship('Profissional', backref='agendamentos')

class Prontuario(db.Model):
    __tablename__ = 'prontuarios'
    
    id_prontuario = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    observacoes = db.Column(db.Text)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    paciente = db.relationship('Paciente', backref='prontuarios')
    profissional = db.relationship('Profissional', backref='prontuarios')