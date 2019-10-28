import { Component, OnInit } from '@angular/core';

import { formatDate } from '@angular/common';
import { AlertController, ToastController } from '@ionic/angular';
import { DatabaseService } from '../services/database.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
})
export class RegistroPage implements OnInit {

  studentUser: any;
	passwordRepetition: string = "";
	maxDate: string = "";
  minDate: string = "";
  
  constructor(private alertCtrl: AlertController,
    private toastCtrl: ToastController,
    private restProvider: DatabaseService,
    private router: Router) { }

  ngOnInit() {
    //this.obtenerMaxDate();
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

}
