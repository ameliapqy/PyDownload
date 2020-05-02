from django.shortcuts import render, redirect
from django.conf import settings
import json, requests
from pytube import YouTube
import os, shutil
from core.models import Video
from django.views.static import serve 
#return the main search page
def search(request):
    return render(request, "search.html", {"query":""})

#display the result by fetching data from youtubeAPI
def result(request):
    if "query" not in request.POST:
        print("no query no action")
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
    videos = []
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    for result in results: 
        title  = result['snippet']['title']
        url = 'https://www.youtube.com/watch?v=' + result["id"]["videoId"]
        thumbnail = result['snippet']['thumbnails']['medium']['url']
        video = Video.objects.create(title=title, url = url, thumbnail = thumbnail)
        videos.append(video)
    if "download" in request.POST:
        print("detected download ")
        url = request.POST["download"]
        download(url, request)
        print("download finished")
        # return render(request, "result.html", {"query":"N/A", "data": []})
    return render(request, "result.html", {"query":query, "data": videos})

#helper method to download youtube video
def download(url, request):
    yt = YouTube(url)
    video = yt.streams.first()
    video.download("downloads")
    # filepath = os.path.join("downloads",video.title+".mp4") 
    # return serve(request, os.path.basename(filepath),os.path.dirname(filepath))


def empty_folder():
    for root, dirs, files in os.walk("downloads"):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
