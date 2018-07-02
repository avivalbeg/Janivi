from django.shortcuts import render

def index(request):
    return render(request,template_name="AboutIndex.html")
# Create your views here.
