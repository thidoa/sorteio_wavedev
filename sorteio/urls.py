from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('participar_sorteio', views.participar_sorteio, name="participar_sorteio"),
    path('sorteio', views.sorteio, name="sorteio"),
    path('sobre', views.sobre, name="sobre"),
    path('realizar_sorteio', views.realizar_sorteio, name="realizar_sorteio"),
]
