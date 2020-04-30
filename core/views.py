from django.shortcuts import render, redirect
import json
from core.static import particles.json
# Create your views here.
def search(request):
    return render(request, "search.html", {"particles": particles.json});

def result(request):
    query = {}
    if request.POST["query"]:
        query = request.POST["query"]
    else:
        query = "N/A"
    return render(request, "result.html", {"query":query});