from django.shortcuts import render

def index(request):
    return render(request,template_name="index.html")

def detail(request):
    return render(request,template)

# Create your views here.
