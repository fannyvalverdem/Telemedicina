import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { InicioSesionPage } from './inicio-sesion.page';
import { RegistroComponent } from '../registro/registro.component';

const routes: Routes = [
  {
    path: '',
    component: InicioSesionPage
  },{
    path: 'register',
    component: RegistroComponent
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [InicioSesionPage,RegistroComponent]
})
export class InicioSesionPageModule {}
