import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { StorageHandlerService } from './storage-handler.service';
import { AlertController, MenuController } from '@ionic/angular';
import { HTTP } from '@ionic-native/http/ngx';


@Injectable({
  providedIn: 'root'
})
export class RestService {

	apiUrl = "https://plataformaaprendizaje.herokuapp.com/";
	//apiUrl = "https://xaandrad.pythonanywhere.com/"; //Dirección del servidor del backend
	zoomApiUrl = "https://api.zoom.us/v2/";

	constructor(private http: HttpClient, private storage: StorageHandlerService,
				private alertCtrl: AlertController, private httpIonic: HTTP
	) {

	}

	headerAuthorization(){
		const header = {
			'Authorization': 'Token ' + this.storage.getKey()
		};
		return new HttpHeaders(header);
	}

	login(user) {
		return new Promise((resolve,reject) => {
			this.http.post(this.apiUrl+'authenticate/', user).subscribe(data => {
				resolve(data);
				//console.log(data);
			}, err => {
				reject(err);
				console.log(err);
			});
		});
	}

	getPersonInformation() {
		return new Promise((resolve,reject) => {
			console.log(this.storage.getId());
			console.log(this.storage.getIsStudent());
			console.log(this.storage.getIsTutor());
			if (this.storage.getIsStudent()){
				this.http.get(this.apiUrl+`api/student_users/${this.storage.getId()}`,
				{headers: this.headerAuthorization()}).subscribe(data => {
					resolve(data);
				}, err => {
					reject(err);
				})
			} else if (this.storage.getIsTutor()){
				this.http.get(this.apiUrl+`api/tutor_users/${this.storage.getId()}`,
				{headers: this.headerAuthorization()}).subscribe(data => {
					resolve(data);
				}, err => {
					reject(err);
				})
			}
			
		});
	}

	getCourses() {
		//console.log(this.headerAuthorization());
		return new Promise((resolve,reject) => {
			console.log("Antes del if dentro de getCourses");
			console.log(this.storage.getIsStudent());
			console.log(this.storage.getIsTutor());
			if (this.storage.getIsStudent()){
				console.log("Entró a IsStudent");
				this.http.get(this.apiUrl+`api/student_users/${this.storage.getId()}/courses/`,
					{headers: this.headerAuthorization()}).subscribe(data => {
					resolve(data);
				}, err => {
					reject(err);
				})
			} else if (this.storage.getIsTutor()) {
				console.log("Es tutor");
				this.http.get(this.apiUrl+`api/tutor_users/${this.storage.getId()}/courses/`,
					{headers: this.headerAuthorization()}).subscribe(data => {
					resolve(data);
				}, err => {
					reject(err);
				})
			}
		});
	}

	getCourse(courseId) {
		return new Promise((resolve,reject) => {
			this.http.get(this.apiUrl+`api/courses/${courseId}`,
			{headers: this.headerAuthorization()}).subscribe(data => {
				resolve(data);
			}, err => {
				reject(err);
			})
		})
	}

	updateProfile(profile) {
		return new Promise((resolve,reject) => {
			this.http.put(
				this.apiUrl+`api/profiles/${profile.id}/`,
				profile,
				{headers: this.headerAuthorization()}).subscribe(data => {
					resolve(data);
				}, err => {
					reject(err);
				})
		})
	}

	updatePersonalData(info) {
		return new Promise((resolve,reject) => {
			if (this.storage.getIsStudent()){

				this.http.put(
					this.apiUrl+`api/student_users/${this.storage.getId()}/`,
					info,
					{headers: this.headerAuthorization()}).subscribe(data => {
						resolve(data);
					}, err => {
						reject(err);
					})
			} else if (this.storage.getIsTutor()) {
				this.http.put(
					this.apiUrl+`api/tutor_users/${this.storage.getId()}/`,
					info,
					{headers: this.headerAuthorization()}).subscribe(data => {
						resolve(data);
					}, err => {
						reject(err);
					})
			}
		});
	}

	getClassVideoSession(classId) {
		return new Promise((resolve,reject) => {
			this.http.get(this.apiUrl+`api/course_classes/${classId}/session`,
				{headers: this.headerAuthorization()}).subscribe(data => {
					console.log("AH1");
					resolve(data);
				}, err => {
					console.log("AH2");
					reject(err);
				})
		});
	}

	registerStudent(estudiante) {
		return new Promise ((resolve,reject) => {
			this.http.post(this.apiUrl+"api/student_users/",estudiante).subscribe(data => {
				resolve(data);
			},err => {
				reject(err);
			})
		});
	}

	getStatuses() {
		return new Promise((resolve,reject) => {
			this.http.get(this.apiUrl+"api/statuses/").subscribe(data => {
				resolve(data);
			}, err => {
				reject(err);
			})
		});
	}

	async updateZoomToken() {
		const params = {};
		const headers = {'Authorization': 'Token ' + this.storage.getKey()};
		await this.httpIonic.get(this.apiUrl + `api/token/`,params,headers)
		.then(data => {
			this.storage.setZoomToken(JSON.parse(data.data)['token']);
			this.storage.setZoomUserId(JSON.parse(data.data)['user_id']);
		})
		.catch(error => {
			this.storage.setZoomToken("");
			this.storage.setZoomUserId("");
			this.showAlert("Ha ocurrido un error intentando obtener los elementos necesarios.<br/>Inténtelo de nuevo.")
		})
	}

	async getZoomAccessToken() {
		await this.updateZoomToken();
		if (this.storage.getZoomUserId() != "" && this.storage.getZoomToken() != "") {
			var userId = this.storage.getZoomUserId();
			const url = this.zoomApiUrl + `users/${userId}/token?type=zak`;
			const params = {};
			const headers = {'Authorization': 'Bearer ' + this.storage.getZoomToken()};

			await this.httpIonic.get(url,params,headers)
			.then(data => {
				console.log("Get ZAK correcto");
				console.log(data.status);
				console.log(data.data);
				this.storage.setZoomAccessToken(JSON.parse(data.data)['token']); 
				console.log(data.headers);
			})
			.catch(error => {
				console.log("Get ZAK Error");
				console.log(error.status);
				console.log(error.error);
				this.storage.setZoomAccessToken(""); 
				console.log(error.headers);
			});
		} else {
			this.storage.setZoomAccessToken(""); 
		}
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
