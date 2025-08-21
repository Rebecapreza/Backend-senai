from django.urls import path
from .views import *
urlpatterns = [
    path ('Autores', AutoresView.as_view()),
    path ('autoeres', visualizacao_autor),
    path ('Editora', EditoraView.as_view()),
    path ('Livro', LivroView.as_view()),

    path ('autores/<int:pk>', AutoresDetailView.as_view()),
    path ('Editora/<int:pk>', EditoraDetailView.as_view()),
    path ('Livro/<int:pk>', LivroDetailView.as_view())
]