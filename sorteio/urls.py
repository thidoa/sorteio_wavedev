from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sorteio', views.sorteio, name="sorteio"),
    path('sobre', views.sobre, name="sobre"),
]
