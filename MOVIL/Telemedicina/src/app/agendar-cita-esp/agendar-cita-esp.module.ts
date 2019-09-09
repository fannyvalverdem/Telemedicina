import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { AgendarCitaEspPage } from './agendar-cita-esp.page';

const routes: Routes = [
  {
    path: '',
    component: AgendarCitaEspPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [AgendarCitaEspPage]
})
export class AgendarCitaEspPageModule {}
