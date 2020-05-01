from django.shortcuts import render, redirect
from django.conf import settings
import json, requests
# Create your views here.
def search(request):
    return render(request, "search.html", {"query":""})

def result(request):
    if "query" not in request.POST:
        return render(request, "result.html", {"query":"N/A", "data": []})
        
    query = request.POST["query"]

    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'q': query,
        'key': settings.YOUTUBE_API_KEY,
        'maxResults' : 10,
        'type': 'video'
    }
    all_data = []
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    for result in results: 
        curr_data = {
            'title' : result['snippet']['title'],
            'url' : 'https://www.youtube.com/watch?v=' + result["id"]["videoId"],
            'thumbnail' : result['snippet']['thumbnails']['medium']['url']
        }
        all_data.append(curr_data)
    return render(request, "result.html", {"query":query, "data": all_data})