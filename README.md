# Turn any public YouTube playlist into a Spotify playlist
Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![Image](https://github.com/clipchak/YouTubePlaylistToSpotifyPlaylist/blob/master/images/workingGif.gif)  |  ![](https://...Ocean.png)


This project is based on [TheComeUp's Tutorial](https://www.youtube.com/watch?v=7J_qcttfnJA) that took a person's "liked video" playlist on YouTube and turned it into a Spotify playlist. The difference between [TheComeUp's project](https://github.com/TheComeUpCode/SpotifyGeneratePlaylist) and this project is: 
- Can take **any** public YouTube song playlist and move it to Spotify (not just liked videos)
- Loops through to include **every** song on the playlist
- Uses publically available information - you don't have to go through the more confusing/difficult process of authorizing your YouTube account 
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
   * Your Spotify User ID is just the username you created your Spotify account as
   * To get your Spotify Oauth token visit this url here: [Get Oauth](https://developer.spotify.com/console/post-playlists/) and click the Get Token button
   ![Image](https://github.com/clipchak/YouTubePlaylistToSpotifyPlaylist/blob/master/images/spotifyOauth.png)
3. Enable Oauth For Youtube and download the client_secrets.json
   * You can follow [this tutorial](https://www.youtube.com/watch?v=V4KqpIX6pdI&t) and YouTube's own [guide](https://developers.google.com/youtube/v3/getting-started/). All you need is the basic API key and not the OAuth 2.0 Client ID. Once you collect it, put it in the secrets.py file.
4. Find a YouTube playlist and collect its ID. The ID is the mix of characters after &list= and BEFORE &index (if it is there) in the link of the YouTube playlist.

   ![Image](https://github.com/clipchak/YouTubePlaylistToSpotifyPlaylist/blob/master/images/playlistID.png)
   
   Put this ID in the create_playlist.py file in the get_playlist_videos function where it says:
   ```
   playlistId = "INSERT ANY PUBLIC YOUTUBE SONG PLAYLIST ID",
   ```
5. Run the file 
   ```
   python3 create_playlist.py
   ```
   * it should run automatically and print the songs as it loops through the playlist
   * check your spotify account and the playlist should be there. **Not all songs will be available on Spotify **
   
## TODO
- Add user input to paste a link to a playlist
- Add user input to customize the name of the playlist that goes to Spotify

## Troubleshooting
- If you are given a ```KeyError```, it is probably because your Spotify Oauth token expired. Refer to the second bulletpoint of Step 2 in Setup and paste in a new token to your program
- If a certain song wasn't added from the YouTube playlist to the Spotify playlist, it is because the song was either not available on Spotify or the creator of the YouTube video did not put the correct information in the video's metadata. 
