from marshmallow import Schema, fields, validate

class ProfissionalSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    usuario = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    especialidade = fields.Str(validate=validate.Length(max=100))
    created_at = fields.DateTime(dump_only=True)

class PacienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    telefone = fields.Str(validate=validate.Length(max=20))
    email = fields.Email()
    data_nascimento = fields.Date()
    created_at = fields.DateTime(dump_only=True)

class AgendamentoSchema(Schema):
    id = fields.Int(dump_only=True)
    id_paciente = fields.Int(required=True)
    id_profissional = fields.Int(required=True)
    data_agendamento = fields.Date(required=True)
    hora_agendamento = fields.Time(required=True)
    observacoes = fields.Str()
    status = fields.Str(validate=validate.OneOf(['agendado', 'cancelado', 'realizado']))
    created_at = fields.DateTime(dump_only=True)
    paciente = fields.Nested(PacienteSchema, dump_only=True)
    profissional = fields.Nested(ProfissionalSchema, dump_only=True)

class ProntuarioSchema(Schema):
    id_prontuario = fields.Int(dump_only=True)
    data_criacao = fields.DateTime(dump_only=True)
    id_paciente = fields.Int(required=True)
    id_profissional = fields.Int(required=True)
    observacoes = fields.Str()
    data_atualizacao = fields.DateTime(dump_only=True)
    paciente = fields.Nested(PacienteSchema, dump_only=True)
    profissional = fields.Nested(ProfissionalSchema, dump_only=True)

class LoginSchema(Schema):
    usuario = fields.Str(required=True)
    senha = fields.Str(required=True)