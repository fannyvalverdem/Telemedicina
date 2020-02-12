import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DatabaseService } from '../services/database.service';

@Component({
  selector: 'app-miscitas',
  templateUrl: './miscitas.page.html',
  styleUrls: ['./miscitas.page.scss'],
})
export class MiscitasPage implements OnInit {

  citas_agendadas=[];
  citas_pasadas=[];
  constructor(private storage: StorageHandlerService, private db: DatabaseService) { }

  ngOnInit() {
    this.db.listarCitasPacientes();
    this.citas_agendadas=this.storage.getListaCitasAgendadas();
    console.log(this.citas_agendadas);

    

  }

}
