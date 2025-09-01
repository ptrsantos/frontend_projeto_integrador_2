import { Component, AfterViewInit } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { AnalyticsService } from '../analytics.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-analytics-dashboard',
  templateUrl: './analytics-dashboard.component.html',
  styleUrls: ['./analytics-dashboard.component.css']
})
export class AnalyticsDashboardComponent implements AfterViewInit {
  public appointmentsByDayOfWeekChart: any;
  public appointmentsByTimeOfDayChart: any;
  public serviceTypeDistributionChart: any;
  public monthlyAppointmentTrendChart: any;
  public performanceRadarChart: any;

  // KPIs
  public totalAppointments: number = 0;
  public averageAppointmentsPerDay: number = 0;
  public peakHour: string = '';

  constructor(private analyticsService: AnalyticsService, private router: Router) { 
    Chart.register(...registerables);
  }

  ngAfterViewInit(): void {
    // Existing charts
    this.analyticsService.getAppointmentsByDayOfWeekMock().subscribe((data: { day: string, count: number }[]) => {
      this.createAppointmentsByDayOfWeekChart(data);
      this.calculateDailyKPIs(data);
    });

    this.analyticsService.getAppointmentsByTimeOfDayMock().subscribe((data: { time: string, count: number }[]) => {
      this.createAppointmentsByTimeOfDayChart(data);
      this.findPeakHour(data);
    });

    // New charts
    this.analyticsService.getServiceTypeDistributionMock().subscribe((data: { type: string, count: number }[]) => {
      this.createServiceTypeDistributionChart(data);
    });

    this.analyticsService.getMonthlyAppointmentTrendMock().subscribe((data: { month: string, count: number }[]) => {
      this.createMonthlyAppointmentTrendChart(data);
    });

    this.analyticsService.getPerformanceComparisonMock().subscribe((data: { category: string, score: number }[]) => {
      this.createPerformanceRadarChart(data);
    });
  }

  // Existing methods...
  createAppointmentsByDayOfWeekChart(data: { day: string, count: number }[]){
    const labels = data.map(item => item.day);
    const counts = data.map(item => item.count);

    this.appointmentsByDayOfWeekChart = new Chart("appointmentsByDayOfWeekChart", {
      type: 'bar', 
      data: {
        labels: labels,
        datasets: [
          {
            label: "Agendamentos",
            data: counts,
            backgroundColor: '#667eea',
            borderRadius: 10
          }
        ]
      },
      options: {
        aspectRatio: 2.5,
        responsive: true,
        plugins: {
          title: { display: false }
        }
      }
    });
  }

  createAppointmentsByTimeOfDayChart(data: { time: string, count: number }[]){
    const labels = data.map(item => item.time);
    const counts = data.map(item => item.count);

    this.appointmentsByTimeOfDayChart = new Chart("appointmentsByTimeOfDayChart", {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: "Agendamentos por Horário",
            data: counts,
            backgroundColor: 'rgba(118, 75, 162, 0.2)',
            borderColor: '#764ba2',
            tension: 0.4,
            fill: true
          }
        ]
      },
      options: {
        aspectRatio: 2.5,
        responsive: true,
        plugins: {
          title: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }

  // New chart methods
  createServiceTypeDistributionChart(data: { type: string, count: number }[]){
    const labels = data.map(item => item.type);
    const counts = data.map(item => item.count);

    this.serviceTypeDistributionChart = new Chart("serviceTypeDistributionChart", {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: counts,
          backgroundColor: [
            '#FF6384', 
            '#36A2EB', 
            '#FFCE56', 
            '#4BC0C0', 
            '#9966FF'
          ]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Distribuição de Tipos de Serviço'
          }
        }
      }
    });
  }

  createMonthlyAppointmentTrendChart(data: { month: string, count: number }[]){
    const labels = data.map(item => item.month);
    const counts = data.map(item => item.count);

    this.monthlyAppointmentTrendChart = new Chart("monthlyAppointmentTrendChart", {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Tendência Mensal de Agendamentos',
          data: counts,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1,
          fill: true
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Tendência de Agendamentos Mensais'
          }
        }
      }
    });
  }

  createPerformanceRadarChart(data: { category: string, score: number }[]){
    const labels = data.map(item => item.category);
    const scores = data.map(item => item.score);

    this.performanceRadarChart = new Chart("performanceRadarChart", {
      type: 'radar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Desempenho por Categoria',
          data: scores,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgb(255, 99, 132)',
          pointBackgroundColor: 'rgb(255, 99, 132)'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Comparativo de Desempenho'
          }
        }
      }
    });
  }

  // KPI Calculation Methods
  calculateDailyKPIs(data: { day: string, count: number }[]){
    this.totalAppointments = data.reduce((sum, item) => sum + item.count, 0);
    this.averageAppointmentsPerDay = this.totalAppointments / data.length;
  }

  findPeakHour(data: { time: string, count: number }[]){
    const peakHourData = data.reduce((prev, current) => 
      (prev.count > current.count) ? prev : current
    );
    this.peakHour = peakHourData.time;
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('userType');
    this.router.navigate(['/login']);
  }
}