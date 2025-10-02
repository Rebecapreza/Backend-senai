import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { EditoraService } from '../../services/editoras.services';
import { Editora } from '../../models/editora'; // se o modelo Editora estiver no mesmo arquivo
import { AuthService } from '../../services/auth.services';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Editoras</h1>

      <!-- Estado de carregamento -->
      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (e of editoras(); track e.id) {
            <li style="margin:.25rem 0">
              <strong>{{ e.editora }}</strong><br>
              @if (e.cnpj) { • CNPJ: {{ e.cnpj }} }<br>
              @if (e.endereco) { • Endereço: {{ e.endereco }} }<br>
              @if (e.telefone) { • Telefone: {{ e.telefone }} }<br>
              @if (e.email) { • Email: {{ e.email }} }<br>
              @if (e.site) { • Site: <a href="{{ e.site }}" target="_blank">{{ e.site }}</a> }
            </li>
          }
        </ul>
      }

      <nav style="margin-top:1rem">
        <a routerLink="/">Voltar ao início</a>
      </nav>
    </section>
  `
})
export class EditorasPage {
  private svc = inject(EditoraService);
  private auth = inject(AuthService);   // Ver o token
  editoras = signal<Editora[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    console.log("Token de acesso: ", this.auth.token());
    
    this.svc.listar().subscribe({
      next: (data) => { this.editoras.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar editoras'); this.carregando.set(false); }
    });
  }
}
