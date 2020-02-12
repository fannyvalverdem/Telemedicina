import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DatabaseService } from '../services/database.service';


@Component({
  selector: 'app-agendar-cita-conf',
  templateUrl: './agendar-cita-conf.page.html',
  styleUrls: ['./agendar-cita-conf.page.scss'],
})
export class AgendarCitaConfPage implements OnInit {
  especialidad=this.storage.getEspecialidad();
  selected: any;
  citas_agendadas: any = {id: this.storage.getId(), object: this.selected }
  postobject: any = {especialidad: "",paciente_id:{},doctor_id:{},detalle:{}};
  
  constructor(private http: HttpClient,private db: DatabaseService,private storage: StorageHandlerService) { }

  ngOnInit() {
    this.getPaciente();
    this.postobject["especialidad"]=this.storage.getEspecialidad();
    this.selected= this.storage.getSelectedAppoinment();
    this.crearDetalle();   
    this.postobject["doctor_id"]=this.selected["doctor"];
    this.crearDetalle();
    console.log(this.postobject);
    
    
  }

  

  passingFinal(){
    
    this.http.post('http://127.0.0.1:8000/api/consulta/',this.postobject).subscribe(data => {     
      console.log(data);
    }, err => {
      
      console.log(err);
    });
    
    
  }

  getPaciente(){
    
		this.http.get('http://127.0.0.1:8000/api/paciente/').subscribe(data => {
		 
		  for(var i in data){
			console.log(data[i]["user_id"]["id"]);
			console.log(this.storage.getId());
			if(data[i]["user_id"]["id"]==this.storage.getId()){
				  console.log(data[i]);
				  this.postobject["paciente_id"]=data[i];             
			  }   
		  }
					
			}, err => {     
			  console.log(err);
			
		}); 
    }
    
    crearDetalle(){
      var detalle = {
        "fecha_reser": "",
        "fecha_prog": "",
        "precio": 0,
        "hora": "",
        "calificacion": 0,
        "zoom": 0
      
      }
      var offset= new Date().getTimezoneOffset()*60*1000;
      var fecha_reserva=(new Date(Date.now() - offset)).toISOString().substr(0,10);
      detalle["fecha_reser"]=fecha_reserva;
      detalle["fecha_prog"]=this.selected["fecha"];
      detalle["hora"]=this.selected["hora"]+":00"
      detalle["zoom"]=this.selected["id"];
      detalle["precio"]=this.selected["doctor"]["tarifa"]["precio"];
      this.postobject["detalle"]=detalle;

    }

  



}
