import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';

@Component({
  selector: 'app-miscitas',
  templateUrl: './miscitas.page.html',
  styleUrls: ['./miscitas.page.scss'],
})
export class MiscitasPage implements OnInit {

  citas_agendadas=[];
  citas_pasadas=[];
  constructor(private storage: StorageHandlerService) { }

  ngOnInit() {
    this.citas_agendadas=this.storage.getListaCitasAgendadas();
    

  }

}
