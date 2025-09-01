import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main-dashboard',
  templateUrl: './main-dashboard.component.html',
  styleUrls: ['./main-dashboard.component.css']
})
export class MainDashboardComponent implements OnInit {
  userType: string | null = null;
  activeSection = 'agendamento';
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

  ngOnInit() {
    this.minDate = new Date().toISOString().split('T')[0];
    // Em um cenário real, você buscaria o userType do serviço de autenticação
    this.userType = localStorage.getItem('userType'); // Exemplo simples
  }

  logout() {
    localStorage.removeItem('token'); // Remover token de autenticação
    localStorage.removeItem('userType'); // Remover tipo de usuário
    this.router.navigate(['/login']);
  }

  setActiveSection(section: string) {
    this.activeSection = section;
  }

  onSubmit() {
    if (new Date(this.formData.data) < new Date()) {
      this.erro = 'Não é possível agendar para datas passadas.';
      return;
    }
    
    this.sucesso = `Consulta agendada com sucesso para ${this.formatDate(this.formData.data)} às ${this.formData.hora}!`;
    this.erro = '';
    
    this.formData = {
      profissional: '',
      data: '',
      hora: '',
      nome: '',
      email: '',
      telefone: ''
    };
  }

  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
  }

  formatTime(timeString: string): string {
    return timeString.substring(0, 5);
  }
}
