import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctoresfavPage } from './doctoresfav.page';

describe('DoctoresfavPage', () => {
  let component: DoctoresfavPage;
  let fixture: ComponentFixture<DoctoresfavPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DoctoresfavPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DoctoresfavPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
