import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-agendar-cita-med',
  templateUrl: './agendar-cita-med.page.html',
  styleUrls: ['./agendar-cita-med.page.scss'],
})
export class AgendarCitaMedPage implements OnInit {
  
  public form = [
    { val: 'Doctor 1', isChecked: false },
    { val: 'Doctor 2', isChecked: false },
    { val: 'Doctor 3', isChecked: false }
  ];

  constructor() { }

  ngOnInit() {
  }

}
