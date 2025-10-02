import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LivroService } from '../../services/livro.services';  // Serviço para livros
import { Livro } from '../../model/livro';  // Modelo de Livro
import { AuthService } from '../../services/auth.services';
import { DecimalPipe } from '@angular/common';


@Component({
  standalone: true,
  imports: [RouterLink, DecimalPipe],
  styleUrl: './livros.component.css',
  template: `
    <section style="max-width:900px;margin:2rem auto;padding:0 1rem">
      <h1>Livros</h1>

      <!-- Estado de carregamento -->
      @if (carregando()) {
        <p>Carregando…</p>
      } @else if (erro()) {
        <p style="color:#c62828">{{ erro() }}</p>
      } @else {
        <ul style="padding-left:1.25rem">
          @for (livro of livros(); track livro.id) {
            <li style="margin:.25rem 0">
              <strong>{{ livro.titulo }}</strong> <br>
              @if (livro.autor) { • Autor: {{ livro.autor.nome }} {{ livro.autor.sobrenome }} }<br>
              @if (livro.ano) { • Ano: {{ livro.ano }} }<br>
              @if (livro.isbn) { • ISBN: {{ livro.isbn }} }<br>
              @if (livro.preco) { • Preço: R$ {{ livro.preco | number:'1.2-2' }} }<br>
              @if (livro.editora) { • Editora: {{ livro.editora.editora }} }<br>
              @if (livro.descricao) { <div style="color:#555">{{ livro.descricao }}</div> }
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
export class LivrosPage {
  private svc = inject(LivroService);  // Serviço de livros
  private auth = inject(AuthService);   // Ver o token
  livros = signal<Livro[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    console.log("Token de acesso: ", this.auth.token());

    // Carregar livros
    this.svc.listar().subscribe({
      next: (data) => { 
        this.livros.set(data); 
        this.carregando.set(false); 
      },
      error: () => { 
        this.erro.set('Falha ao carregar livros'); 
        this.carregando.set(false); 
      }
    });
  }
}
