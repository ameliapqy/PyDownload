from django.shortcuts import render, redirect

# Create your views here.
def search(request):
    return render(request, "search.html", {});

def result(request):
    query = {}
    if request.POST["query"]:
        query = request.POST["query"]
    else:
        query = "N/A"
    return render(request, "result.html", {"query":query});