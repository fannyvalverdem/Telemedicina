import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { AgendarCitaConfPage } from './agendar-cita-conf.page';

const routes: Routes = [
  {
    path: '',
    component: AgendarCitaConfPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [AgendarCitaConfPage]
})
export class AgendarCitaConfPageModule {}
