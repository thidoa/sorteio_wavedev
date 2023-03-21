from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sorteios', views.sorteios, name="sorteios"),
    path('participar_sorteio', views.participar_sorteio, name="participar_sorteio"),

]
