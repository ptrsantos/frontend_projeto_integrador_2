import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalyticsDashboardComponent } from './analytics/analytics-dashboard/analytics-dashboard.component';
import { LoginComponent } from './components/login/login.component';
import { MainDashboardComponent } from './components/main-dashboard/main-dashboard.component';
import { PsychologistGuard } from './guards/psychologist.guard';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'dashboard', component: MainDashboardComponent },
  { path: 'analytics-dashboard', component: AnalyticsDashboardComponent, canActivate: [PsychologistGuard] },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: '**', redirectTo: '/login' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
