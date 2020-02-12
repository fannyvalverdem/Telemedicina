import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { DatabaseService } from '../services/database.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { debug } from 'util';
import { analyzeAndValidateNgModules } from '@angular/compiler';

@Component({
  selector: 'app-agendar-cita-med',
  templateUrl: './agendar-cita-med.page.html',
  styleUrls: ['./agendar-cita-med.page.scss'],
})
export class AgendarCitaMedPage implements OnInit {
  espec: string;
  fecha: string;
  hora: string;
  matchesp: any = [];
  selected: any;


  constructor(private http: HttpClient,private storage: StorageHandlerService,private db: DatabaseService) { }

  ngOnInit() {
    this.espec= this.storage.getEspecialidad();
    this.fecha=this.storage.getFechaCons();
    this.hora=this.storage.getHoraCons();
    this.getMatchEspecialidades();
    

    
  }


  getDoctoresHorarios(){
    this.http.get('http://127.0.0.1:8000/api/especialidad/').subscribe(data => {
      
      
    }, err => {     
      console.log(err);
  });
  }

  getMatchEspecialidades(){
    var doctorid;
		this.http.get('http://127.0.0.1:8000/api/match_especialidades/').subscribe(data => {
      for(var i in data){        
          if(data[i]["especialidad"]["nombre"]==this.espec){
            
            doctorid=data[i]["doctor"]["id"];
            this.getCitaMedica(doctorid);            
          }
          
        
      }
      console.log(data);
      
       
		}, err => {     
		  console.log(err);
		
    });
      
	
    }
    
    getCitaMedica(id){
      var horacliente= new Date();
      horacliente.setHours(Number(this.hora.substr(0,2)));
      horacliente.setMinutes(Number(this.hora.substr(3,2)));
      console.log(this.hora);
      console.log(this.fecha);

      this.http.get('http://127.0.0.1:8000/api/citas_medico/').subscribe(data => {
      for(var i in data){
          var horaapi=new Date();
          horaapi.setHours(Number(data[i]["hora"].substr(0,2)));
          horaapi.setMinutes(Number(data[i]["hora"].substr(3,2)));
        if(data[i]["fecha"]==this.fecha && horacliente<horaapi && data[i]["doctor"]["id"]==id ){
              data[i]["hora"]=  data[i]["hora"].substr(0,5)     
              this.matchesp.push(data[i]);            
        }   
      }
      

      
      console.log(this.matchesp);

		  
		        
		}, err => {     
		  console.log(err);
		
    }); 

    }

    

    passingSelected(){
      
      this.storage.setSelectedAppoinment(this.matchesp[this.selected]);
    }

    


}
