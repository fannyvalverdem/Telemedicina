import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MiscitasPage } from './miscitas.page';

describe('MiscitasPage', () => {
  let component: MiscitasPage;
  let fixture: ComponentFixture<MiscitasPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MiscitasPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MiscitasPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
