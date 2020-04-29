from django.shortcuts import render, redirect

# Create your views here.
def search(request):
    return render(request, "search.html", {});