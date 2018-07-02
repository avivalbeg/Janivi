from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Graph
from django.http import Http404
# Create your views here.
def index(request):
    all_graphs = Graph.objects.all()
    template= loader.get_template('graph/index.html')
    context = {
        'all_graphs' : all_graphs,
    }
    return HttpResponse(template.render(context,request))

def detail(request,graph_id):
    try:
        graph = Graph.objects.get(pk=graph_id)
        context = {"graph":graph}
        return render(request,"graph/graph.html",context = context)
    except:
            raise Http404