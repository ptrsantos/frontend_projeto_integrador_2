import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class PsychologistGuard implements CanActivate {

  constructor(private router: Router) {}

  canActivate(): boolean {
    const userType = localStorage.getItem('userType');
    
    if (userType === 'psychologist') {
      return true;
    } else {
      this.router.navigate(['/dashboard']);
      return false;
    }
  }
}