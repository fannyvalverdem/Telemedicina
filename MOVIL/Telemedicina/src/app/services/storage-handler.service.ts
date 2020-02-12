import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { AngularDelegate } from '@ionic/angular';

@Injectable({
	providedIn: 'root'
})
export class StorageHandlerService {
	citas_agendadas=[];
	citas_pasadas=[];
	idPaciente: any;
	
	especialidad: string;
	fechacons: string;
	usuario: any;
	horacons: string;
	selectedapp: {};
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

	setAll(key, id) {
		this.key = key;
		this.id = id;
		this.writeInStorage("key", key);
		this.writeInStorage("id", id);
		console.log(key);
		console.log(id);
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

	setEspecialidad(value: string){
		this.especialidad= value;
	}

	getEspecialidad(){
		return this.especialidad;
	}

	setFechaCons(value: string){
		this.fechacons= value;
	}

	setUsuario(value){
		this.usuario=value;
	}

	setIdPaciente(value){
		this.idPaciente=value;
	}

	getIdPaciente(){
		return this.idPaciente;
	}

	getUsuario(){
		return this.usuario;
	}



	getFechaCons(){
		return this.fechacons;
	}

	setHoraCons(value: string){
		this.horacons= value;
	}

	getHoraCons(){
		return this.horacons;
	}

	setSelectedAppoinment(value){
		this.selectedapp= value;
	}

	getSelectedAppoinment(){
		return this.selectedapp;
	}

	addToCitasAgendadas(value){
		this.citas_agendadas.push(value);

	}

	getListaCitasAgendadas(){
		return this.citas_agendadas
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
