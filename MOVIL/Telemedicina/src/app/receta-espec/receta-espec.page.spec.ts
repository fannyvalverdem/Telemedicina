import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecetaEspecPage } from './receta-espec.page';

describe('RecetaEspecPage', () => {
  let component: RecetaEspecPage;
  let fixture: ComponentFixture<RecetaEspecPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecetaEspecPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecetaEspecPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
