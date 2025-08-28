from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #get/post
    path ('Autores', AutoresView.as_view()),
    path ('autoeres', visualizacao_autor),
    path ('Editora', EditoraView.as_view()),
    path ('Livro', LivroView.as_view()),
    path ('Buscar', AutoresView.as_view()),

    #update/ delete
    path ('autores/<int:pk>', AutoresDetailView.as_view()),
    path ('Editora/<int:pk>', EditoraDetailView.as_view()),
    path ('Livro/<int:pk>', LivroDetailView.as_view()),

    #token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
