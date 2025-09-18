import { Injectable, Inject, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Autor } from "../models/autor";
import { enviroment } from "../environments/enviroment";


@Injectable({providedIn: 'root'})
export class AutoresService{
    private http = inject(HttpClient) 
    private base = enviroment.apiBase

    listar(): Observable<Autor[]>{
        const url = `${this.base}autores`
        return this.http.get<Autor[]>(url)
    }
}