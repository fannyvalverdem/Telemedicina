import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { Router, RouterEvent } from '@angular/router';
import { Zoom } from '@ionic-native/zoom';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  
  ZOOM_API_KEY="fRb1YgwnRT6ASYvVxSMwOg";
  ZOOM_API_SECRET="t1CUHWdU2bzbVmL1aT9HFdfuke0SRP8Og6VZ";
  zoomService = Zoom;

  pages=[
    {
      title:'Contactenos',
      url:'/contacto'
    },
    {
      title:'Mis Citas',
      url:'/miscitas'
    }
  ];

  selectedPath = '';

  constructor(
    private router: Router,
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar
  ) {
    this.router.events.subscribe((event:RouterEvent)=> {
      this.selectedPath = event.url;
    });
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();

      //Inicialización de servicio Zoom
      this.zoomService.initialize(this.ZOOM_API_KEY,this.ZOOM_API_SECRET)
      .then((success: any) => {
        this.presentToast("Servicio de videoconferencia inicializado correctamente.",2000)
      })
      .catch((error: any) => {
        this.presentToast("Ocurrió un error al inicializar el servicio de Zoom.\nNo podrá visualizar ninguna clase activa en vivo.",4000);
      });
    });
  }

  async presentToast(mensaje,duracion) {
    const toast = await this.toastCtrl.create({
    message: mensaje,
    duration: duracion
    });
    toast.present();
  }


}
