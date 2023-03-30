from django.urls import path
from .views import index, Categoria, Animal

urlpatterns = [
    path('index.html', index, name = 'index.html'),
    path('', Categoria, name = 'Categoria'),
    path('', Animal, name = 'Animal'),
]
