import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Editora, Autor, Livro

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo_livros", default="population/livros.csv")
        parser.add_argument("--arquivo_editoras", default="population/editoras.csv")
        parser.add_argument("--arquivo_autores", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df_autores = pd.read_csv(o["arquivo_autores"], encoding="utf-8-sig")
        df_editoras = pd.read_csv(o["arquivo_editoras"], encoding="utf-8-sig")
        df_livros = pd.read_csv(o["arquivo_livros"], encoding="utf-8-sig")

        df_autores.columns = [c.strip().lower().lstrip("\ufeff") for c in df_autores.columns]
        df_editoras.columns = [c.strip().lower().lstrip("\ufeff") for c in df_editoras.columns]
        df_livros.columns = [c.strip().lower().lstrip("\ufeff") for c in df_livros.columns]

        if o['truncate']:
            Livro.objects.all().delete()

        criados = 0
        for r in df_livros.itertuples(index=False):
            try:
                partes = r.autor.strip().split()
                nome = partes[0]
                sobrenome = " ".join(partes[1:])
                autor = Autor.objects.filter(nome=nome, sobrenome=sobrenome).first()
                if not autor:
                    self.stdout.write(self.style.WARNING(
                        f"Ignorado livro '{r.titulo}': autor '{r.autor}' não encontrado"
                    ))
                    continue

                editora = Editora.objects.get(editora=r.editora.strip())
                livro, created = Livro.objects.get_or_create(
                    titulo=r.titulo.strip(),
                    defaults={
                        "subtitulo": getattr(r, "subtitulo", ""),
                        "autor": autor,
                        "editora": editora,
                        "isbn": getattr(r, "isbn", ""),
                        "descricao": getattr(r, "descricao", ""),
                        "idioma": getattr(r, "idioma", ""),
                        "ano": getattr(r, "ano_publicacao", None),
                        "paginas": getattr(r, "paginas", None),
                        "preco": getattr(r, "preco", None),
                        "estoque": getattr(r, "estoque", None),
                        "desconto": getattr(r, "desconto", None),
                        "disponivel": getattr(r, "disponivel", True),
                        "dimensoes": getattr(r, "dimensoes", ""),
                        "peso": getattr(r, "peso", None),
                    }
                )
                criados += int(created)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao criar livro '{r.titulo}': {e}"))

        self.stdout.write(self.style.SUCCESS(f"Criados: {criados} livros"))