### CIS192 Final Project
### PyDownloader

Group Members:

1. Qingyuan Peng (Pennkey: pqy)

2. Yijie Lu (Pennkey: luyijie)

3. Yuzhou Lin (Pennkey: yzlin)


Description: Welcome to PyDownloader--A simple downloader to download any youtube video you want! As you enter the keywords in the search bar, PyDownloader will crawl the top ten videos that contain the entered keywords from Youtube. You will be able to download those videos into a specific folder on your computer right away. Enjoy your video crawling time!

## Instruction on how to run PyDownloader in the terminal:

cd Pydownload-master

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver

The (local) url to the Pydownloader webpage: http://127.0.0.1:8000/


## Functionality:

One class definition: Video

Two magic methods: 1. def __str__(self)  2. def __init__(self, title, url, thumbnail)

Two non-trivial first-party packages: 1. requests  2.  os  3. shutil

Two non-trivial third-party packages: 1. Django  2. pytube


## Code Structure

In models.py, we defined the Video class, which contains the title, url, and thumbnail of the corresponding youtube video.

In search.html, we use the user-entered query to search the related youtube videos.

We then pass the list of videos to result.html using the Video class. 

When a user clicks the download button, we will then use the download helper function in view.py to download the .mp4 file to the server’s ‘downloads’ folder.
