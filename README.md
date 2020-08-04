# YouTubePlaylistToSpotifyPlaylist
This project is based on [TheComeUp's Tutorial](https://www.youtube.com/watch?v=7J_qcttfnJA) that took a person's "liked video" playlist on YouTube and turned it into a Spotify playlist. The difference between [TheComeUp's project](https://github.com/TheComeUpCode/SpotifyGeneratePlaylist) and this project is: 
- Can take **any** public YouTube song playlist and move it to Spotify (not just liked videos)
- Loops through to include **every** song on the playlist
- You don't have to go through the confusing/difficult process of authorizing a YouTube account (uses publically available information)
- Uses Facebook's web crawler for better reliability

## Technologies 
- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Requests Library](https://requests.readthedocs.io/en/master/)
- [Youtube_dl v 2020.7.28](https://github.com/ytdl-org/youtube-dl/)
- [The Facebook Crawler](https://developers.facebook.com/docs/sharing/webmasters/crawler/)

## Setup
1. Install Dependencies 
```
pip3 install -r requirements.txt
```
or if using [PyCharm IDE](https://www.jetbrains.com/pycharm/), it will ask you to install the dependencies automatically.
2. Add your Spotify User ID and Oauth Token from Spotfiy to the secrets.py file
  * Your Spotify User ID is just the name you used to make your Spotify account
