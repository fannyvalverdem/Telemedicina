import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DoctoresfavPage } from '../doctoresfav/doctoresfav.page';

@Component({
  selector: 'app-agendar-cita-conf',
  templateUrl: './agendar-cita-conf.page.html',
  styleUrls: ['./agendar-cita-conf.page.scss'],
})
export class AgendarCitaConfPage implements OnInit {
  especialidad=this.storage.getEspecialidad();
  selected: any;
  postobject: any = {estado: "agendado",paciente_id: {},doctor_id:{},detalle:{}};
  
  constructor(private http: HttpClient,private storage: StorageHandlerService) { }

  ngOnInit() {
    this.selected= this.storage.getSelectedAppoinment();
    this.postobject["doctor_id"]=this.selected["doctor"];
    console.log(this.selected);
    console.log(this.postobject);
    
  }

  

  passingFinal(){
    this.storage.addToCitasAgendadas(this.selected);
    this.http.post('http://127.0.0.1:8000/api/consulta/',this.postobject).subscribe(data => {     
      console.log(data);
    }, err => {
      
      console.log(err);
    });
    
    
  }


}
