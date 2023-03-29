# 

1. # 🎵Spot-Down-Tube🎵

   This script allows you to download music from a Spotify playlist using `yt-dlp` and `youtube`.

   ## 📋 How it works

   1. The script takes a Spotify playlist URL and uses `BeautifulSoup` to scrape the track information from the page.
   2. The track information is then used to search for the first result on YouTube.
   3. The script then calls an external program, `yt-dlp`, to download the audio from the YouTube link.
   4. The downloaded audio is saved in an `mp3` format in a `musics` folder.

   ## 🛠️ Dependencies

   - `requests`
   - `urllib`
   - `re`
   - `os`
   - `BeautifulSoup`
   - `unidecode`
   - `yt-dlp`

   ## 💻 Environment

   This script was tested in a Python 3.10 environment.

   ## 🔧 Installation

   1. Make sure you have Python 3.10 installed on your system.
   2. Install the dependencies by running: `pip install requests beautifulsoup4 unidecode yt-dlp`.
   3. Clone or download this repository.
   4. Gimme some stars :star:

   ## 🚀 Usage

   1. Make sure you have all the dependencies installed.
   2. Replace the `URL` variable with the Spotify playlist URL you want to download.
   3. Run the script.`python3 spot_down_tube.py`

   Enjoy your music! 🎶
