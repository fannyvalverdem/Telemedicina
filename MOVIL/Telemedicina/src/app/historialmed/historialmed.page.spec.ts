import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HistorialmedPage } from './historialmed.page';

describe('HistorialmedPage', () => {
  let component: HistorialmedPage;
  let fixture: ComponentFixture<HistorialmedPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HistorialmedPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HistorialmedPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
