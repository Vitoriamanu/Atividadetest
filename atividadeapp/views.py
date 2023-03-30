from django.shortcuts import render
from .models import Categoria, Animal

def index(request):
    return render(request, 'index.html')

def Categoria(request):
    return render()

def Animal(request):
    return render()