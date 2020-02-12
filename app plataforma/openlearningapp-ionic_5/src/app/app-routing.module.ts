import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { LoadingScreenComponent } from './loading-screen/loading-screen.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'initLoading',
    pathMatch: 'full'
  },
  {
    path: 'home',
    loadChildren: './home/home.module#HomePageModule'
  },
  { 
    path: 'authentication', 
    loadChildren: './inicio-sesion/inicio-sesion.module#InicioSesionPageModule' 
  },
  { 
    path: 'perfil',
    loadChildren: './perfil/perfil.module#PerfilPageModule' 
  },
  {
    path: 'initLoading',
    component: LoadingScreenComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
