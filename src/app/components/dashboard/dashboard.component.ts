import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  @Input() userType: string | null = null;
  activeSection = 'agendamento';

  constructor(private router: Router) {}

  get isPsychologist(): boolean {
    return this.userType === 'psychologist';
  }

  get isPatient(): boolean {
    return this.userType === 'patient';
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('userType');
    this.router.navigate(['/login']);
  }
}