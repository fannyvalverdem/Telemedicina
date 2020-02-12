import { Component, OnInit } from '@angular/core';
import { StorageHandlerService } from '../storage-handler.service';
import { Router } from '@angular/router';
import { LoadingController } from '@ionic/angular';

@Component({
selector: 'app-loading-screen',
templateUrl: './loading-screen.component.html',
styleUrls: ['./loading-screen.component.scss'],
})
export class LoadingScreenComponent implements OnInit {

	constructor(private storageHandler: StorageHandlerService,
				private router: Router,
				private loadingController: LoadingController) { }

	async ngOnInit() {
		var isEmpty = await this.storageHandler.isEmpty();

		if (!isEmpty) {
			await this.storageHandler.fillVariables();
			this.router.navigate(['/home'],{ skipLocationChange: true, replaceUrl: true });
		} else {
			this.router.navigate(['/authentication'],{ skipLocationChange: true, replaceUrl: true });
		}
	}

	async ionViewDidEnter() {
        var isEmpty = await this.storageHandler.isEmpty();

		if (!isEmpty) {
			await this.storageHandler.fillVariables();
			this.router.navigate(['/home'],{ skipLocationChange: true, replaceUrl: true });
		} else {
			this.router.navigate(['/authentication'],{ skipLocationChange: true, replaceUrl: true });
		}
    }

	async presentLoading() {
		const loading = await this.loadingController.create({
			message: 'Loading...',
			duration: 2000,
		});
		await loading.present();

	}

}
