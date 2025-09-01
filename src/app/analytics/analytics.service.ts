import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AnalyticsService {

  constructor() { }

  getAppointmentsByDayOfWeekMock(): Observable<{ day: string, count: number }[]> {
    const mockData = [
      { day: 'Domingo', count: 50 },
      { day: 'Segunda-feira', count: 120 },
      { day: 'Terça-feira', count: 150 },
      { day: 'Quarta-feira', count: 100 },
      { day: 'Quinta-feira', count: 130 },
      { day: 'Sexta-feira', count: 110 },
      { day: 'Sábado', count: 70 }
    ];
    
    return of(mockData);
  }

  getAppointmentsByTimeOfDayMock(): Observable<{ time: string, count: number }[]> {
    const mockData = [
      { time: '08:00', count: 30 },
      { time: '09:00', count: 50 },
      { time: '10:00', count: 70 },
      { time: '11:00', count: 60 },
      { time: '12:00', count: 40 },
      { time: '13:00', count: 55 },
      { time: '14:00', count: 80 },
      { time: '15:00', count: 75 },
      { time: '16:00', count: 65 },
      { time: '17:00', count: 45 }
    ];
    return of(mockData);
  }

  getServiceTypeDistributionMock(): Observable<{ type: string, count: number }[]> {
    const mockData = [
      { type: 'Consulta Médica', count: 150 },
      { type: 'Exame de Sangue', count: 80 },
      { type: 'Vacinação', count: 120 },
      { type: 'Fisioterapia', count: 60 },
      { type: 'Psicologia', count: 40 }
    ];
    return of(mockData);
  }

  getMonthlyAppointmentTrendMock(): Observable<{ month: string, count: number }[]> {
    const mockData = [
      { month: 'Jan', count: 200 },
      { month: 'Fev', count: 220 },
      { month: 'Mar', count: 180 },
      { month: 'Abr', count: 250 },
      { month: 'Mai', count: 300 },
      { month: 'Jun', count: 280 }
    ];
    return of(mockData);
  }

  getPerformanceComparisonMock(): Observable<{ category: string, score: number }[]> {
    const mockData = [
      { category: 'Tempo de Espera', score: 4.5 },
      { category: 'Qualidade do Atendimento', score: 4.8 },
      { category: 'Infraestrutura', score: 4.2 },
      { category: 'Resolução de Problemas', score: 4.6 },
      { category: 'Acessibilidade', score: 4.3 }
    ];
    return of(mockData);
  }
}