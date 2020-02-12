import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { formatDate } from '@angular/common';
import { AlertController } from '@ionic/angular';
import { Router } from '@angular/router';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {

	person: any = {profile:{}}
	modifiedPerson: any = {profile:{}}
	modificar = false;
	maxDate: string = "";
	minDate: string = "";


	constructor(private restProvider: RestService,
				private alertCtrl: AlertController,
				private router: Router) {
	}

	ngOnInit() {
	}

	ionViewWillEnter() {
		this.modificar = false;
		this.getPersonInformation();
	}

	ionViewDidLeave() {
		this.modificar = false;
		this.person = {profile:{}};
	}

	obtenerMaxDate() {
		var time = formatDate(Date(),"yyyy-MM-dd","EN");
		var splittedTime = time.split("-");
		splittedTime[0] = String(Number(splittedTime[0])-18);
		this.maxDate = splittedTime.join("-");
		splittedTime[0] = String(Number(splittedTime[0])-92);
		this.minDate = splittedTime.join("-");
	}

	getPersonInformation() {
		this.restProvider.getPersonInformation().then(data => {
			this.person = data;
			this.modifiedPerson = data;
			console.log(this.person);
			this.showAlert("Información cargada correctamente.")
		}, err => {
			this.showAlert("Ha ocurrido un error.");
		})
	}

	async showAlert(mensaje) {
		const alert = await this.alertCtrl.create({
			header: "Sistema",
			message: mensaje,
			buttons: ["OK"]
		});
		await alert.present();
	}

	cambiarModificar() {
		if (this.modificar) this.modifiedPerson = this.person;
		this.modificar = !this.modificar;
        //console.log("¿Son iguales?: " + this.person === this.modifiedPerson);
	}

	modificarDatos() {

		if (this.ingresoValido()) {
			const envio = {
				'id': this.modifiedPerson.id,
				'email': this.modifiedPerson.email,
				'photo': this.modifiedPerson.photo,
				'id_status': this.modifiedPerson.status.id,
				'profile': this.modifiedPerson.profile
			}
			this.restProvider.updatePersonalData(envio).then(data => {
				this.showAlert("Actualización de datos hecha correctamente");
				this.modificar = false;
			}, err => {
				if(err['status']==400){
					var mensaje = "Corrija los siguientes errores:<br/><br/>";
					var hayMensajes = false;
					if (!(err['error']['email'] === undefined)){
						mensaje = mensaje + "- Campo E-mail: " + err['error']['email'][0] + "<br/>";
						hayMensajes = true;
					}
					if (!(err['error']['profile'] === undefined)){
						if(!(err['error']['profile']['names']=== undefined)){
							mensaje = mensaje + "- Campo Nombres: " + err['error']['profile']['names'][0] + "<br/>";
						}
						if(!(err['error']['profile']['last_names']=== undefined)){
							mensaje = mensaje + "- Campo Apellidos: " + err['error']['profile']['last_names'][0] + "<br/>";
						}
						if(!(err['error']['profile']['identification']=== undefined)){
							mensaje = mensaje + "- Campo Identificación: " + err['error']['profile']['identification'][0] + "<br/>";
						}
						if(!(err['error']['profile']['dob']=== undefined)){
							mensaje = mensaje + "- Campo Fecha: " + err['error']['profile']['dob'][0] + "<br/>";
						}
						if(!(err['error']['profile']['phone']=== undefined)){
							mensaje = mensaje + "- Campo Teléfono: " + err['error']['profile']['phone'][0] + "<br/>";
						}
						hayMensajes = true;
					}
					this.showAlert(mensaje);
				}else if(err['status']==500){
					this.showAlert("Ha ocurrido un error interno en el servidor.<br/>Por favor, vuelva a intentar completar la acción en unos segundos.");			
				}else{
					this.showAlert("Ha ocurrido un error desconocido. <br/>Por favor, vuelva a intentar completar la acción en unos segundos.");
				}
				console.log(err);
			})
		}

		
	}

	ingresoValido(): boolean {
		var mensaje: string = "Hay los siguientes errores en su ingreso de datos:"
		var valido: boolean = true;
		
		if (this.modifiedPerson.email == "") {
			mensaje = mensaje + "<br/>- Debe ingresar un e-mail.";
			valido = false;
		}

		if (this.modifiedPerson.profile.dob == "") {
			mensaje = mensaje + "<br/>- Debe ingresar una fecha de nacimiento.";
			valido = false;
		}

		if (this.modifiedPerson.profile.phone == "") {
			mensaje = mensaje + "<br/>- Debe ingresar un número de teléfono.";
			valido = false;
		}

		if (this.modifiedPerson.profile.address == "") {
			mensaje = mensaje + "<br/>- Debe ingresar una dirección de domicilio.";
			valido = false;
		}

		if (this.modifiedPerson.profile.names == "") {
			mensaje = mensaje + "<br/>- Debe ingresar al menos un nombre válido.";
			valido = false;
		}

		if (this.modifiedPerson.profile.last_names == "") {
			mensaje = mensaje + "<br/>- Debe ingresar al menos un apellido válido.";
			valido = false;
		}

		if (!valido){
			this.showAlert(mensaje);
		}

		return valido;
	}
}
