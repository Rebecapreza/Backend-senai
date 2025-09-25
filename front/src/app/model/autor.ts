export interface Autor {
    id: number;
    nome: string;
    sobrenome?: string | null;
    data_nasc?: string | null;
    nacion?: string | null;
    biogra?: string | null;
}
