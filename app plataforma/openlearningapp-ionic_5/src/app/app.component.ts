import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { Platform, AlertController, ToastController } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { Zoom } from '@ionic-native/zoom';

import { StorageHandlerService } from './storage-handler.service';


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {

  ZOOM_API_KEY="HhlUkNfUparvu1SWWvhBy1pWETd1gpET8bTn";
  ZOOM_API_SECRET="F7MvF80TRMVybvTX4XjwSiyCLBISvEoSLduC";
  zoomService = Zoom;

  public appPages = [
    {
      title: 'Cursos',
      url: '/home',
      icon: 'list'
    },
    {
      title: 'Perfil',
      url: '/perfil',
      icon: 'person'
    }
  ];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private storageHandler: StorageHandlerService,
    private alertCtrl: AlertController,
    private router: Router,
    private toastCtrl: ToastController
  ) {
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

  async showAlert(mensaje) {
    const alert = await this.alertCtrl.create({
      header: "Sistema",
      message: mensaje,
      buttons: ["OK"]
    });
    await alert.present();
  }

  async cerrarSesion() {
    await this.storageHandler.clear();
    //this.storageHandler = new StorageHandler(this.storage);
    this.showAlert("Ha cerrado sesión satisfactoriamente.");
    this.router.navigate([''],{ skipLocationChange: true, replaceUrl: true });
  }

  async presentToast(mensaje,duracion) {
    const toast = await this.toastCtrl.create({
    message: mensaje,
    duration: duracion
    });
    toast.present();
  }

  navegar(ruta) {
    this.router.navigate([ruta],{ skipLocationChange: true, replaceUrl: true })
  }
}
