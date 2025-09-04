import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autores

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("ufeff") for c in df.columns]

        if o["truncate"]: Autores.objects.all().delete()

        df["nome"]= df["nome"].astype(str).str.strip()
        df["sobrenome"]= df["sobrenome"].astype(str).str.strip()
        df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce", format="%Y-%m-%d").dt.date
        df["nacionalidade"] = df.get("nacionalidade", "").astype(str).str.strip()

        df = df.query("nome != '' and sobrenome != '' " )
        df = df.dropna(subset=['data_nascimento'])

        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Autores.objects.update_or_create(
                    nome = r.nome, sobrenome=r.sobrenome, data_nascimento=r.data_nascimento,
                    defaults={"nacionalidade": r.nacionalidade}
                )

                criados += int(created)
                atualizados += (not created)
            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [Autores(
                nome=r.nome, sobrenome=r.sobrenome, data_nascimento=r.data_nascimento, nacionalidade=r.nacionalidade
            ) for r in df.itertuples(index=False)]     

            Autores.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Criado: {len(objs)}'))