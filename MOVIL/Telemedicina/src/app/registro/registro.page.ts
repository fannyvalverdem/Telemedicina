import { Component, OnInit } from '@angular/core';
import { DatabaseService } from '../services/database.service';
import { StorageHandlerService } from '../services/storage-handler.service';
import { AlertController, MenuController } from '@ionic/angular'
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
})
export class RegistroPage implements OnInit {
  persona_id: any = {nombre: "", apellido:"", telefono:""};
  user: any = { username: "", password: "", persona_id:{}};
  
  constructor(private restProvider: DatabaseService,
    private storageHandler: StorageHandlerService,
    private alertCtrl: AlertController,
    private router: Router,
    private menuController: MenuController) { }

  ngOnInit() {
    this.menuController.enable(false, 'optionPages');
  }

  ionViewDidEnter() {
    this.menuController.enable(false, 'optionPages');
  }

  async registro() {
    var retorno: boolean = false;
    if (this.inputsVacios()) {
      this.showAlert("Debe rellenar todos los campos.");
      retorno = false; //Retorna este False cuando no ingresó al menos un campo.
    } else {
      await this.restProvider.registro(this.user, this.persona_id)
        .then(data => {
          
          this.showAlert("Se registró de forma correcta");
          this.router.navigate(['/principal'], { replaceUrl: true });
          retorno = true; //Retorna True si inició sesión de forma correcta
        }, err => {
          this.showAlert(JSON.parse(JSON.stringify(err))['error']);
          retorno = false; //Retorna este False si las credenciales son incorrectas.
        })
    }

    console.log(retorno);
    return retorno;
  }

  async showAlert(mensaje) {
    const alert = await this.alertCtrl.create({
      header: "Sistema",
      message: mensaje,
      buttons: ["OK"]
    });
    await alert.present();
  }

  irARegistrar() {
    this.router.navigate(['registro']);
  }

  inputsVacios() {
    if (this.user.nombre == "" || this.user.apellido == "" || this.user.telefono == "" || this.user.username == "" || this.user.password == "") {
      return true;
    }
    return false;
  }

  async probarZak() {
    await this.restProvider.getZoomAccessToken();
    this.showAlert(this.storageHandler.getZoomAccessToken());
  }
}
