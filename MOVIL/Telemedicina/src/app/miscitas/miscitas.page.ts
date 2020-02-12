import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DatabaseService } from '../services/database.service';
import { AlertController, ToastController } from '@ionic/angular';
import { Zoom } from '@ionic-native/zoom';

@Component({
  selector: 'app-miscitas',
  templateUrl: './miscitas.page.html',
  styleUrls: ['./miscitas.page.scss'],
})
export class MiscitasPage implements OnInit {
  
  zoomService = Zoom;
  citas_agendadas=[];
  citas_pasadas=[];
  constructor(private storage: StorageHandlerService, private db: DatabaseService) { }

  ngOnInit() {
    this.db.listarCitasPacientes();
    this.citas_agendadas=this.storage.getListaCitasAgendadas();
    console.log(this.citas_agendadas);

  }

  async joinMeeting(meetingId) {
    console.log(meetingId);

    //Unión al meeting
    let options = {};
    this.zoomService.joinMeeting(meetingId,"","Paciente",options)
    .then((success: any) => {
      this.presentToast("Videoconferencia exitosa.",1000)
    },)
    .catch((error: any) => {
      this.showAlert(error)
    });
    
  }
}