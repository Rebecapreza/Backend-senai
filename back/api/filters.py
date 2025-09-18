import django_filters as df
from django.db.models import Q
from .models import Autor

class AutorFIlter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nacionalidade = df.CharFilter(method='nacionalidade', lookup_expr='iexact')

    def filter_nome(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q (nome_icontains = value) | Q (sobrenome_icontains = value))
    
    def nacionalide(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q (nacionalidade_icontains = value))
    
    class Meta:
        model = Autor
        fields = []
