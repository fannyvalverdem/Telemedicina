import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RestService } from '../rest.service';
import { Zoom } from '@ionic-native/zoom';
import { AlertController, ToastController } from '@ionic/angular';
import { StorageHandlerService } from '../storage-handler.service';

@Component({
  selector: 'app-detalle-curso',
  templateUrl: './detalle-curso.component.html',
  styleUrls: ['./detalle-curso.component.scss'],
})
export class DetalleCursoComponent implements OnInit {

	zak: any;
	course: any = {};
	zoomService = Zoom;
	isTutor = false;
	displayName: string = "";

	constructor(private activatedRoute: ActivatedRoute,
				private restProvider: RestService,
				private storageHandler: StorageHandlerService,
				private alertCtrl: AlertController,
				private toastCtrl: ToastController) {

	}

	ngOnInit() {
		this.isTutor = this.storageHandler.getIsTutor();
		if (this.isTutor) this.displayName = "Tutor";
		else this.displayName = "Estudiante";
		this.getPersonInformation();
		const idCurso = this.activatedRoute.snapshot.paramMap.get('id');
		this.restProvider.getCourse(idCurso).then(data => {
			this.course = data;
			console.log(this.course);
		},err => {
			console.log("ERROR");
		})
	}

	async verVideo(classId) {
		var sessionInfo:any = await this.sessionInfo(classId);
		//console.log(sessionInfo['meeting_number']);

		//Unión al meeting
		let options = {};
		this.zoomService.joinMeeting(sessionInfo['meeting_number'],"",this.displayName,options)
		.then((success: any) => {
			this.presentToast("Ha salido de la videoconferencia.",1000)
		},)
		.catch((error: any) => {
			this.showAlert(error)
		});
		
	}

	async initMeeting(classId) {
		await this.restProvider.getZoomAccessToken();
		if (this.storageHandler.getZoomAccessToken()!=""){
			var sessionInfo:any = await this.sessionInfo(classId);
			let options = {};
			this.zoomService.startMeetingWithZAK(sessionInfo['meeting_number'],this.displayName,this.storageHandler.getZoomToken(),this.storageHandler.getZoomAccessToken(),this.storageHandler.getZoomUserId(),options)
			.then((success: any) => {
				this.presentToast("Ha salido de la videoconferencia.",1000)
			},)
			.catch((error: any) => {
				this.showAlert(error)
			});	
		} else {
			this.showAlert("No se puede iniciar el meeting en este momento.<br/>Por favor, inténtelo de nuevo.")
		}
		
	}

	private async sessionInfo(classId) {
		var session:any = {};
		await this.restProvider.getClassVideoSession(classId)
		.then(data => {
			session = data;
		}, err => {
			this.showAlert("Ocurrió un error al obtener la session.");
		})
		return session;
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

	getPersonInformation() {
		this.restProvider.getPersonInformation().then(data => {
			var parseado = JSON.parse(JSON.stringify(data));
			this.displayName = parseado['profile']['names'] + " " + parseado['profile']['last_names'];
			console.log(parseado);
			console.log(this.displayName);
		}, err => {
			console.log("Ocurrió un error intentando obtener el nombre.");
		})
	}

	doRefresh(event){
		this.getPersonInformation();
		const idCurso = this.activatedRoute.snapshot.paramMap.get('id');
		this.restProvider.getCourse(idCurso).then(data => {
			this.course = data;
			console.log(this.course);
		},err => {
			console.log("ERROR");
		})
		setTimeout(() => {
			console.log('Async operation has ended');
			event.target.complete();
		}, 2000);
	}

	isActive(estado) {
		if(estado == 'ACTIVO') return true;
		return false;
	}
}
