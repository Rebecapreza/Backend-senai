import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autor as Author


class Command(BaseCommand):
    help = "Importa autores de um CSV para o banco de dados"

    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        df = pd.read_csv(options["arquivo"], encoding="utf-8-sig")

        # Normaliza os nomes das colunas
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        # Renomeia colunas do CSV para os campos do model
        rename_map = {
            "autor": "nome",
            "s_autor": "sobrenome",
            "nasc": "data_nasc",
            "nacio": "nacion",
        }
        df = df.rename(columns=rename_map)

        # Garantir que todas as colunas existem
        for col in ["nome", "sobrenome", "data_nasc", "nacion"]:
            if col not in df.columns:
                df[col] = None

        # Limpeza básica
        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()
        df["data_nasc"] = pd.to_datetime(
            df["data_nasc"], errors="coerce", format="%Y-%m-%d"
        ).dt.date
        df["nacion"] = df["nacion"].astype(str).str.strip()

        # Remove inválidos
        df = df.query("nome != '' and sobrenome != ''")
        df = df.dropna(subset=["data_nasc"])

        if options["truncate"]:
            Author.objects.all().delete()

        if options["update"]:
            criados = 0
            atualizados = 0

            for r in df.itertuples(index=False):
                obj, created = Author.objects.update_or_create(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    data_nasc=r.data_nasc,
                    defaults={
                        "nacion": r.nacion,
                        "biogra": getattr(r, "biogra", ""),
                    },
                )
                criados += int(created)
                atualizados += int(not created)

            self.stdout.write(
                self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}")
            )
        else:
            objects = [
                Author(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    data_nasc=r.data_nasc,
                    nacion=r.nacion,
                    biogra=getattr(r, "biogra", ""),
                )
                for r in df.itertuples(index=False)
            ]

            Author.objects.bulk_create(objects, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objects)}"))
