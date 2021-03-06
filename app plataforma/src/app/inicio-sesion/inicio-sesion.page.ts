import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { StorageHandlerService } from '../storage-handler.service';
import { AlertController, MenuController } from '@ionic/angular'
import { Router } from '@angular/router';

@Component({
  selector: 'app-inicio-sesion',
  templateUrl: './inicio-sesion.page.html',
  styleUrls: ['./inicio-sesion.page.scss'],
})
export class InicioSesionPage implements OnInit {

	user:any = {username:"",password:""};

	constructor(private restProvider: RestService,
				private storageHandler: StorageHandlerService,
				private alertCtrl: AlertController,
                private router: Router,
                private menuController: MenuController) {
        
    }

	ngOnInit() {
        this.menuController.enable(false, 'optionPages');
    }

    ionViewDidEnter() {
        this.menuController.enable(false, 'optionPages');
    }

	async iniciarSesion() {
        var retorno:boolean = false;
        if(this.inputsVacios()){
            this.showAlert("Debe rellenar todos los campos.");
            retorno = false; //Retorna este False cuando no ingresó al menos un campo.
        } else {
            await this.restProvider.login(this.user) 
            .then(data =>{
                this.storageHandler.setAll(
                    JSON.parse(JSON.stringify(data))['key'],
                    JSON.parse(JSON.stringify(data))['id'],
                    JSON.parse(JSON.stringify(data))['is_student'],
                    JSON.parse(JSON.stringify(data))['is_staff'],
                    JSON.parse(JSON.stringify(data))['is_tutor']);
                this.showAlert("Inició sesión de forma correcta");
                this.router.navigate(['/home'],{ skipLocationChange: true, replaceUrl: true });
                retorno = true; //Retorna True si inició sesión de forma correcta
            },err => {
                this.showAlert(JSON.parse(JSON.stringify(err))['error']['non_field_errors'][0]);
                retorno = false; //Retorna este False si las credenciales son incorrectas.
            })
        }

        this.user.username = "";
        this.user.password = "";

        //console.log(retorno);
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

    irARegistrar(){
        this.router.navigate(['/authentication/register']);
    }

    inputsVacios() {
        if (this.user.username == "" || this.user.password == "") {
            return true;
        }
        return false;
    }

    async probarZak() {
        await this.restProvider.getZoomAccessToken();
        this.showAlert(this.storageHandler.getZoomAccessToken());
    }

}
