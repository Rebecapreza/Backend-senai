import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Editora } from '../models/editora';
import { environment } from '../enviroments/envroments';

@Injectable({ providedIn: 'root' })
export class EditoraService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar(): Observable<Editora[]> {
    const url = `${this.base}api/editoras`;
    return this.http.get<Editora[]>(url);
  }
}
