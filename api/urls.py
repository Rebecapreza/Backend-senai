from django.urls import path
from .views import * 
urlpatterns = [
    path ('Autores', AutoresView.as_view()),
]
