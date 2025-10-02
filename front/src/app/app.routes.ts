import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutoresComponent } from './pages/authors/authors.components';
import { EditorasPage } from './pages/editora/editora.component';
import { LivrosPage } from './pages/livros/livros.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'autores', component: AutoresComponent},
    {path:'editoras', component: EditorasPage },
    {path:'livros', component: LivrosPage }  
];
