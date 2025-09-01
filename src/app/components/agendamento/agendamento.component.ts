import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-agendamento',
  templateUrl: './agendamento.component.html',
  styleUrls: ['./agendamento.component.css']
})
export class AgendamentoComponent implements OnInit {
  @Input() userType: string | null = null;
  
  sucesso = '';
  erro = '';
  minDate = '';
  
  profissionais = [
    { id: 1, nome: 'Cícera Santana' }
  ];
  
  agendamentos = [
    {
      id_paciente: 1,
      paciente: 'Maria Oliveira',
      data_agendamento: '2025-03-15',
      hora_agendamento: '14:00:00'
    },
    {
      id_paciente: 2,
      paciente: 'João Santos',
      data_agendamento: '2025-03-16',
      hora_agendamento: '10:30:00'
    }
  ];
  
  formData = {
    profissional: '',
    data: '',
    hora: '',
    nome: '',
    email: '',
    telefone: ''
  };

  constructor(private router: Router) { }

  get isPsychologist(): boolean {
    return this.userType === 'psychologist';
  }

  ngOnInit() {
    this.minDate = new Date().toISOString().split('T')[0];
  }

  onSubmit() {
    // Validação básica
    if (new Date(this.formData.data) < new Date()) {
      this.erro = 'Não é possível agendar para datas passadas.';
      return;
    }
    
    // Simular sucesso
    this.sucesso = `Consulta agendada com sucesso para ${this.formatDate(this.formData.data)} às ${this.formData.hora}!`;
    this.erro = '';
    
    // Limpar formulário
    this.formData = {
      profissional: '',
      data: '',
      hora: '',
      nome: '',
      email: '',
      telefone: ''
    };
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('userType');
    this.router.navigate(['/login']);
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
  }

  formatTime(timeString: string): string {
    return timeString.substring(0, 5);
  }

  verProntuario(idPaciente: number) {
    // Implementar navegação para prontuário
    console.log('Ver prontuário do paciente:', idPaciente);
  }
}