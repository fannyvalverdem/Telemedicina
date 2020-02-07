import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';

@Component({
  selector: 'app-agendar-cita-conf',
  templateUrl: './agendar-cita-conf.page.html',
  styleUrls: ['./agendar-cita-conf.page.scss'],
})
export class AgendarCitaConfPage implements OnInit {

  selected:{};
  
  constructor(private storage: StorageHandlerService) { }

  ngOnInit() {
    this.selected= this.storage.getSelectedAppoinment();
    console.log(typeof(this.selected));
  }


}
