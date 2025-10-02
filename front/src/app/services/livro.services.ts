import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Livro } from '../model/livro';
import { environment } from '../../environments/environments';

@Injectable({ providedIn: 'root' })
export class LivroService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar(): Observable<Livro[]> {
    const url = `${this.base}api/Livro`;
    return this.http.get<Livro[]>(url);
  }
}
