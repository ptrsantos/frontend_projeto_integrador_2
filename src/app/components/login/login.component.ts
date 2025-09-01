import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  showLogin = false;
  loginError = '';
  
  credentials = {
    usuario: '',
    senha: ''
  };

  constructor(private router: Router) { }

  ngOnInit() {
    // Verificar se já está logado, redirecionar para o dashboard principal
    if (localStorage.getItem('token') && localStorage.getItem('userType')) {
      this.router.navigate(['/dashboard']);
    }
  }

  showLoginForm() {
    this.showLogin = true;
  }

  selectUserType(type: string) {
    // Para pacientes, ir direto para o dashboard com tipo 'patient'
    localStorage.setItem('userType', type);
    localStorage.setItem('token', 'fake-patient-token'); // Simula um login de paciente
    this.router.navigate(['/dashboard']);
  }

  onLogin() {
    if (this.credentials.usuario === 'cicera.santana' && this.credentials.senha === 'senha123') {
      localStorage.setItem('userType', 'psychologist');
      localStorage.setItem('token', 'fake-psychologist-token');
      this.loginError = '';
      this.router.navigate(['/dashboard']);
    } else {
      this.loginError = 'Credenciais inválidas!';
    }
  }
}