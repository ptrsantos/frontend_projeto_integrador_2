# API REST Clínica Mentalize

API REST desenvolvida em Python/Flask para o sistema de gerenciamento da Clínica Mentalize.

## Funcionalidades

- **Autenticação JWT**: Login seguro para profissionais
- **Gestão de Pacientes**: CRUD completo
- **Agendamentos**: Criação, edição e consulta de agendamentos
- **Prontuários**: Gerenciamento de prontuários eletrônicos
- **Profissionais**: Gestão de usuários do sistema

## Instalação.

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Configurar variáveis de ambiente no arquivo `.env`

3. Executar a aplicação:
```bash
python app.py
```

## Endpoints da API

### Autenticação
- `POST /api/auth/login` - Login do profissional
- `GET /api/auth/me` - Dados do usuário logado

### Pacientes
- `GET /api/pacientes/` - Listar pacientes
- `POST /api/pacientes/` - Criar paciente
- `GET /api/pacientes/{id}` - Buscar paciente
- `PUT /api/pacientes/{id}` - Atualizar paciente
- `DELETE /api/pacientes/{id}` - Excluir paciente

### Agendamentos
- `GET /api/agendamentos/` - Listar agendamentos
- `POST /api/agendamentos/` - Criar agendamento
- `GET /api/agendamentos/{id}` - Buscar agendamento
- `PUT /api/agendamentos/{id}` - Atualizar agendamento
- `DELETE /api/agendamentos/{id}` - Excluir agendamento
- `GET /api/agendamentos/hoje` - Agendamentos de hoje

### Prontuários
- `GET /api/prontuarios/` - Listar prontuários
- `POST /api/prontuarios/` - Criar prontuário
- `GET /api/prontuarios/{id}` - Buscar prontuário
- `PUT /api/prontuarios/{id}` - Atualizar prontuário
- `DELETE /api/prontuarios/{id}` - Excluir prontuário
- `GET /api/prontuarios/paciente/{id}` - Prontuários de um paciente

### Profissionais
- `GET /api/profissionais/` - Listar profissionais
- `POST /api/profissionais/` - Criar profissional
- `GET /api/profissionais/{id}` - Buscar profissional
- `PUT /api/profissionais/{id}` - Atualizar profissional
- `DELETE /api/profissionais/{id}` - Excluir profissional

## Exemplo de uso

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"usuario": "cicera.santana", "senha": "senha123"}'
```

### Criar agendamento
```bash
curl -X POST http://localhost:5000/api/agendamentos/ \
  -H "Content-Type: application/json" \
  -d '{
    "paciente_nome": "João Silva",
    "paciente_telefone": "11999999999",
    "id_profissional": 1,
    "data_agendamento": "2025-05-15",
    "hora_agendamento": "14:00:00",
    "observacoes": "Primeira consulta"
  }'
```

## Tecnologias

- Flask 2.3.3
- SQLAlchemy
- JWT Extended
- Marshmallow
- PyMySQL
- CORS