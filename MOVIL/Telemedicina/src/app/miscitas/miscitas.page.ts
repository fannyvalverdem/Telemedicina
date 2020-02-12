import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DatabaseService } from '../services/database.service';
import { Zoom } from '@ionic-native/zoom';

@Component({
  selector: 'app-miscitas',
  templateUrl: './miscitas.page.html',
  styleUrls: ['./miscitas.page.scss'],
})
export class MiscitasPage implements OnInit {
  
  zoomService = Zoom;
  displayName: string = "";
  citas_agendadas=[];
  citas_pasadas=[];
  constructor(private storage: StorageHandlerService, private db: DatabaseService) { }

  ngOnInit() {
    this.db.listarCitasPacientes();
    this.citas_agendadas=this.storage.getListaCitasAgendadas();
    console.log(this.citas_agendadas);

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
}
