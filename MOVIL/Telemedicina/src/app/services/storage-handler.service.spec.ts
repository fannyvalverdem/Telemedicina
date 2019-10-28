import { TestBed } from '@angular/core/testing';

import { StorageHandlerService } from './storage-handler.service';

describe('StorageHandlerService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: StorageHandlerService = TestBed.get(StorageHandlerService);
    expect(service).toBeTruthy();
  });
});
