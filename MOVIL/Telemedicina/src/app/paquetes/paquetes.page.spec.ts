import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PaquetesPage } from './paquetes.page';

describe('PaquetesPage', () => {
  let component: PaquetesPage;
  let fixture: ComponentFixture<PaquetesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PaquetesPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PaquetesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
