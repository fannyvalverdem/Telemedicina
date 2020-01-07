import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: './login/login.module#LoginPageModule' 
  },
  { path: 'login', loadChildren: './login/login.module#LoginPageModule' },
  { path: 'registro', loadChildren: './registro/registro.module#RegistroPageModule' },
  { path: 'emergencia', loadChildren: './emergencia/emergencia.module#EmergenciaPageModule' },
  { path: 'principal', loadChildren: './principal/principal.module#PrincipalPageModule' },
  { path: 'agendar-cita-esp', loadChildren: './agendar-cita-esp/agendar-cita-esp.module#AgendarCitaEspPageModule' },
  { path: 'agendar-cita-med', loadChildren: './agendar-cita-med/agendar-cita-med.module#AgendarCitaMedPageModule' },
  { path: 'agendar-cita-conf', loadChildren: './agendar-cita-conf/agendar-cita-conf.module#AgendarCitaConfPageModule' },  { path: 'perfil', loadChildren: './perfil/perfil.module#PerfilPageModule' },
  { path: 'videollamada', loadChildren: './videollamada/videollamada.module#VideollamadaPageModule' },
  { path: 'pago', loadChildren: './pago/pago.module#PagoPageModule' },
  { path: 'receta', loadChildren: './receta/receta.module#RecetaPageModule' },
  { path: 'doctoresfav', loadChildren: './doctoresfav/doctoresfav.module#DoctoresfavPageModule' },
  { path: 'historialmed', loadChildren: './historialmed/historialmed.module#HistorialmedPageModule' },
  { path: 'receta-espec', loadChildren: './receta-espec/receta-espec.module#RecetaEspecPageModule' },
  { path: 'paquetes', loadChildren: './paquetes/paquetes.module#PaquetesPageModule' },
  { path: 'contacto', loadChildren: './contacto/contacto.module#ContactoPageModule' }

];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
