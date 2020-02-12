import { Component, OnInit, ModuleWithComponentFactories } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import * as m from 'moment';


 

@Component({
  selector: 'app-agendar-cita-esp',
  templateUrl: './agendar-cita-esp.page.html',
  styleUrls: ['./agendar-cita-esp.page.scss'],
})
export class AgendarCitaEspPage implements OnInit {
  posts: any = [];
  opcion: string;  
  fecha: any;
  hora: any ;
  
  offset= new Date().getTimezoneOffset()*60*1000;
  d=(new Date(Date.now() - this.offset)).toISOString().substr(0,10);
  h=(new Date(Date.now() - this.offset)).toISOString().substr(11,5);
  
  
  

  constructor(private http: HttpClient,private storage: StorageHandlerService) { }
  
  ngOnInit() {
    this.getEspecialidadAPI();
    
  }

  passingParameters(){
    this.storage.setEspecialidad(this.opcion);
    this.storage.setFechaCons(this.fecha.substr(0,10));
    this.storage.setHoraCons(this.hora.substr(11,5)); 
  }

  showDate(){
    console.log(this.fecha);
  }

  showHour(hora){
    console.log(this.hora);   
  }
 
  
	getEspecialidadAPI() {
		
    this.http.get('http://127.0.0.1:8000/api/especialidad/').subscribe(data => {
      
      console.log(data);
      this.posts=data;
      
    }, err => {     
      console.log(err);
    
  });
}

}
