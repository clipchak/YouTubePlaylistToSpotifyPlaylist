# YouTubePlaylistToSpotifyPlaylist
This project is based on [TheComeUp's Tutorial](https://www.youtube.com/watch?v=7J_qcttfnJA) that took a person's "liked video" playlist on YouTube and turned it into a Spotify playlist. The difference between [TheComeUp's project](https://github.com/TheComeUpCode/SpotifyGeneratePlaylist) and this project is: 
- Can take **any** public YouTube song playlist and move it to Spotify (not just liked videos)
- Loops through to include **every** song on the playlist
- You don't have to go through the confusing/difficult process of authorizing a YouTube account (uses publically available information)
- Uses Facebook's web crawler for more reliability

## Technologies 
- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Requests Library](https://requests.readthedocs.io/en/master/)
- [Youtube_dl v 2020.7.28](https://github.com/ytdl-org/youtube-dl/)
