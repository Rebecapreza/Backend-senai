from django.urls import path
from .views import * 
urlpatterns = [
    path ('Autores', AutoresView.as_view()),
    path ('autoeres', visualizacao_autor)
]
