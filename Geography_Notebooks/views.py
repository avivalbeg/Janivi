from django.shortcuts import render
from .models import Notebook

def index(request):
    Notebooks = Notebook.objects.all()
    context = {
        "Notebooks":Notebooks
    }
    return render(request,template_name="index.html",context=context)

def detail(request):
    return render(request,template)

# Create your views here.
