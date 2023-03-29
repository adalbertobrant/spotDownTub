import requests
import urllib.request
import re
import os
from bs4 import BeautifulSoup
from unidecode import unidecode

# get music and author from a list and return a list of dictionaries
def get_track_info(soup):    
    tracks = soup.find_all('a')
    track_info = []
    dics = []
    for i in range(1,len(tracks)):
      track_info.append(unidecode(tracks[i].text))
    for i in range(0,len(track_info),2):
      pair = {track_info[i], track_info[i+1]}
      dics.append(pair)
    print(dics)
    return dics

# call an external program to download the first audio
def get_you_tub(link):
    if not os.path.exists("musics"):
        os.makedirs("musics")
    os.chdir("musics")
    
    # Get the video title using yt-dlp
    video_title = os.popen(f'yt-dlp --get-title {link}').read().strip()
    # Set the filename for the downloaded audio file
    filename = f"{video_title}.mp3"
    
    # Check if the file already exists
    if not os.path.isfile(filename):
        # Download and extract audio if file doesn't exist
        os.system(f"yt-dlp --verbose -x --audio-format mp3 {link}")
        print(f"Downloaded '{filename}'")
    else:
        print(f"'{filename}' already exists. Skipping download.")
    
    os.chdir("..")
    print("Done - Extracting  :) \0/")

# return the first link from youtube
def search_you_tub(parameters):
  
  html = urllib.request.urlopen("https://www.youtube.com/results/?search_query=" + parameters)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  
  first_link = f"https://youtube.com/watch?v={video_ids[0]}"
  
  return first_link


# write your list here!
URL = "https://open.spotify.com/playlist/37i9dQZF1DX0hWmn8d5pRe#login"

page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

tracks = soup.find_all('a', href=True)

dics = get_track_info(soup)

for i in dics:
  parameters = list(i)
  parameters = '+'.join(['+'.join(element.split()) for element in parameters])
  print(f"Searching for {parameters}...")
  first_link = search_you_tub(parameters)
  get_you_tub(first_link)

print("-----------------------")

print(" ")
print("Enjoy")










