import { Component, OnInit } from '@angular/core';
import { formatDate } from '@angular/common';
import { AlertController, ToastController } from '@ionic/angular';
import { RestService } from '../rest.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.scss'],
})
export class RegistroComponent implements OnInit {

	studentUser: any;
	passwordRepetition: string = "";
	maxDate: string = "";
	minDate: string = "";

	constructor(private alertCtrl: AlertController,
				private toastCtrl: ToastController,
				private restProvider: RestService,
				private router: Router) { }

	ngOnInit() {
		this.obtenerMaxDate();
		this.studentUser = {email:"",
							profile:{names:"",
									 last_names:"",
									 identification:"",
									 gender:"M",
									 dob:"",
									 phone:"",
									 address:""},
							password:"",
							id_status:"1"};
		this.passwordRepetition = "";
	}

	obtenerMaxDate() {
		var time = formatDate(Date(),"yyyy-MM-dd","EN");
		var splittedTime = time.split("-");
		splittedTime[0] = String(Number(splittedTime[0])-18);
		this.maxDate = splittedTime.join("-");
		splittedTime[0] = String(Number(splittedTime[0])-92);
		this.minDate = splittedTime.join("-");
	}

	registrarEstudiante() {
		if(this.ingresoValido()){
			//console.log(this.studentUser);
			
			this.restProvider.registerStudent(this.studentUser)
			.then(data => {
				this.showAlert("Se ha registrado correctamente.");
				this.router.navigate(['']);
			},err => {
				console.log(err);
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
				
			});
			
		} else {
			this.presentToast("Corrija todos los errores.",3000);
		}
		console.log(this.studentUser);
	}

	capturarGenero(value) {
		this.studentUser.profile.gender = value; 
	}

	ingresoValido(): boolean {
		var mensaje: string = "Hay los siguientes errores en su ingreso de datos:"
		var valido: boolean = true;
		//console.log(this.passwordRepetition);
		//console.log(this.studentUser.password);
		if (this.passwordRepetition == "" || this.studentUser.password == "") {
			mensaje = mensaje + "<br/>- No ha ingresado contraseñas válidas.";
			valido = false;
		}
		else if (this.passwordRepetition != this.studentUser.password) {
			mensaje = mensaje + "<br/>- Las contraseñas ingresadas no coinciden.";
			valido = false;
		} else {
			if (this.studentUser.email == "") {
				mensaje = mensaje + "<br/>- Debe ingresar un e-mail.";
				valido = false;
			}

			if (this.studentUser.profile.dob == "") {
				mensaje = mensaje + "<br/>- Debe ingresar una fecha de nacimiento.";
				valido = false;
			}

			if (this.studentUser.profile.phone == "") {
				mensaje = mensaje + "<br/>- Debe ingresar un número de teléfono.";
				valido = false;
			}

			if (this.studentUser.profile.address == "") {
				mensaje = mensaje + "<br/>- Debe ingresar una dirección de domicilio.";
				valido = false;
			}

			if (this.studentUser.profile.names == "") {
				mensaje = mensaje + "<br/>- Debe ingresar al menos un nombre válido.";
				valido = false;
			}

			if (this.studentUser.profile.last_names == "") {
				mensaje = mensaje + "<br/>- Debe ingresar al menos un apellido válido.";
				valido = false;
			}
		}

		console.log(valido);

		if (!valido){
			this.showAlert(mensaje);
		}

		return valido;
	}

	async showAlert(mensaje) {
		const alert = await this.alertCtrl.create({
			header: "Sistema",
			message: mensaje,
			buttons: ["OK"]
		});
		await alert.present();
	}

	async presentToast(mensaje,duracion) {
		const toast = await this.toastCtrl.create({
			message: mensaje,
			duration: duracion
		});
		toast.present();
	}

}
