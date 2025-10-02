import { Autor } from './autor';
import { Editora } from './editora';

export interface Livro {
    id: number;
    titulo: string;
    subtitulo?: string|null;
    autor: Autor;
    editora: Editora;
    isbn: string;
    descricao?: string|null;
    idioma?: string|null;
    ano: number;
    paginas: number;
    preco: number;
    estoque: number;
    desconto?: number|null;
    disponivel: boolean;
    dimensoes?: string|null;
    peso?: number|null;
}
