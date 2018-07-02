from django.shortcuts import render
from .models import Site
from django.http import Http404

def index(request):
    Sites = Site.objects.all()
    context = {
        "Sites":Sites
    }
    return render(request,template_name="JFrontIndex.html",context=context)