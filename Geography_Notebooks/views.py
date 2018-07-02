from django.shortcuts import render
from .models import Notebook
from django.http import Http404

def index(request):
    Notebooks = Notebook.objects.all()
    context = {
        "Notebooks":Notebooks
    }
    return render(request,template_name="AboutIndex.html",context=context)

def detail(request,notebook_id):
    try:
        notebook = Notebook.objects.get(pk=notebook_id)
        return render(request,notebook.notebook_location)
    except:
            raise Http404

# Create your views here.
