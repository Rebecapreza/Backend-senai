export interface Autor{
    id: number; 
    nome: string;
    sobrenome: string;
    data_nasc?: string | null;
    nacion?: string | null;
    biografia?: string | null;
}