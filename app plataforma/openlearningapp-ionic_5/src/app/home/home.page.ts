import { Component } from '@angular/core';
import { RestService } from '../rest.service';
import { Router } from '@angular/router';
import { MenuController, AlertController } from '@ionic/angular'

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
	courses: any = null;

	constructor(private restProvider: RestService,
				private router: Router,
				private alertCtrl: AlertController,
				private menuController: MenuController) {
		
	}
	
	ngOnInit() {
		//this.menuController.enable(true, 'optionPages');
		//this.getCourses();
	}

    ionViewWillEnter() {
    	this.menuController.enable(true, 'optionPages');
        this.getCourses();
    }
	
	getCourses() {
		this.restProvider.getCourses().then(data => {
			console.log(data);
			if(data[0] === undefined) this.courses = null;
			else this.courses = data;
		}, err => {
			console.log("Ocurrió un error");
			console.log(err);
			this.courses = null;
			this.showAlert("Ha ocurrido un error intentando obtener los cursos.<br/> Inténtelo de nuevo actualizando la pantalla.")
		});
	}

	courseDetail(courseId) {
		this.router.navigate([`home/curso/${courseId}`])
	}

	doRefresh(event){
		this.getCourses();
		setTimeout(() => {
			console.log('Async operation has ended');
			event.target.complete();
		}, 2000);
	}

	async showAlert(mensaje) {
		const alert = await this.alertCtrl.create({
			header: "Sistema",
			message: mensaje,
			buttons: ["OK"]
		});
		await alert.present();
	}

}
