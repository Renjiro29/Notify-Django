from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return (request, 'index.html')
