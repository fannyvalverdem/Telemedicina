import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';

import { HomePage } from './home.page';
import { DetalleCursoComponent } from '../detalle-curso/detalle-curso.component'

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild([
      {
        path: '',
        component: HomePage
      },
      {
        path: 'curso/:id',
        component: DetalleCursoComponent
      }
    ])
  ],
  declarations: [HomePage,DetalleCursoComponent]
})
export class HomePageModule {}
