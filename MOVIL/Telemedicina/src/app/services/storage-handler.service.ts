import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';

@Injectable({
	providedIn: 'root'
})
export class StorageHandlerService {

	key: any;
	id: any;
	email: string;
	username: string;
	esUsuario: boolean;
	isStudent: boolean;
	isStaff: boolean;
	isTutor: boolean;
	zoomUserId: string;
	zoomToken: string;
	zoomAccessToken: string;

	constructor(private storage: Storage) {
		this.zoomUserId = "";
		this.zoomToken = "";
		this.zoomAccessToken = "";
	}

	setAll(id, email, username) {
		this.id = id;
		this.email = email;
		this.username = username;
		this.writeInStorage("id", id);
		this.writeInStorage("email", email)
		this.writeInStorage("username", username);
	}

	writeInStorage(key: string, value: any) {
		this.storage.set(key, value);
	}

	public async getValuePromise(key) {
		var retorno;
		await this.storage.get(key).then(
			data => {
				retorno = data;
			});
		return retorno;
	}

	getKey() {
		return this.key;
	}

	setKey(value) {
		this.key = value;
		this.writeInStorage("key", value);
	}

	getId() {
		return this.id;
	}

	setId(value) {
		this.id = value;
		this.writeInStorage("id", value);
	}

	getEsUsuario() {
		return this.esUsuario;
	}

	setEsUsuario(value) {
		this.esUsuario = value;
		this.writeInStorage("esUsuario", value);
	}

	getIsStudent() {
		return this.isStudent;
	}

	setIsStudent(value) {
		this.isStudent = value;
		this.writeInStorage("isStudent", value);
	}

	getIsTutor() {
		return this.isTutor;
	}

	setIsTutor(value) {
		this.isTutor = value;
		this.writeInStorage("isTutor", value);
	}

	getIsStaff() {
		return this.isStaff;
	}

	setIsStaff(value) {
		this.isStaff = value;
		this.writeInStorage("isStaff", value);
	}

	async clear() {
		this.key = null;
		this.id = null;
		this.esUsuario = null;
		this.isStaff = null;
		this.isStudent = null;
		this.isTutor = null;
		await this.storage.clear();
		/*
		this.getValuePromise('key').then(data => {
			this.key = data;
			console.log(this.key);
		})
		this.getValuePromise('id').then(data => {
			this.id = data;
			console.log(this.id);
		})*/
	}

	getZoomUserId() {
		return this.zoomUserId;
	}

	getZoomToken() {
		return this.zoomToken;
	}

	async isEmpty() {
		var longitud = await this.storage.length();
		if (longitud != 0) return false;
		return true;
	}

	async fillVariables() {
		this.key = await this.getValuePromise('key');
		this.id = await this.getValuePromise('id');
		this.id = await this.getValuePromise('esUsuario');
		this.isStaff = await this.getValuePromise('isStaff');
		this.isTutor = await this.getValuePromise('isTutor');
		this.isStudent = await this.getValuePromise('isStudent');
	}

	setZoomUserId(userId) {
		this.zoomUserId = userId;
	}

	setZoomToken(zoomToken) {
		this.zoomToken = zoomToken;
	}

	getZoomAccessToken() {
		return this.zoomAccessToken;
	}

	setZoomAccessToken(token) {
		this.zoomAccessToken = token;
	}
}
