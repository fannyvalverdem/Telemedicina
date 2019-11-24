import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../services/storage-handler.service';
import { Router } from '@angular/router';
import { LoadingController } from '@ionic/angular';

@Component({
  selector: 'app-loadingscreen',
  templateUrl: './loadingscreen.component.html',
  styleUrls: ['./loadingscreen.component.scss'],
})
export class LoadingscreenComponent implements OnInit {

  constructor(private storageHandler: StorageHandlerService,
    private router: Router,
    private loadingController: LoadingController) { }

  async ngOnInit() {
    var isEmpty = await this.storageHandler.isEmpty();

    if (!isEmpty) {
      await this.storageHandler.fillVariables();
      this.router.navigate(['/home'], { skipLocationChange: true, replaceUrl: true });
    } else {
      this.router.navigate(['/authentication'], { skipLocationChange: true, replaceUrl: true });
    }
  }

  async ionViewDidEnter() {
    var isEmpty = await this.storageHandler.isEmpty();

    if (!isEmpty) {
      await this.storageHandler.fillVariables();
      this.router.navigate(['/principal'], { skipLocationChange: true, replaceUrl: true });
    } else {
      this.router.navigate(['/registro'], { skipLocationChange: true, replaceUrl: true });
    }
  }

  async presentLoading() {
    const loading = await this.loadingController.create({
      message: 'Cargando...',
      duration: 2000,
    });
    await loading.present();

  }

}
