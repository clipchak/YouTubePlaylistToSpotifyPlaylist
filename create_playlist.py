import json

import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from exceptions import ResponseException
from secrets import spotify_token, spotify_user_id, api_key

class CreatePlaylist:
    def __init__(self):
        self.youtube_client = self.get_youtube_client()

        #use a customer user agent (facebook's web crawler) because it is more reliable
        youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"

        self.all_song_info = {}

    def get_youtube_client(self):
        youtube_client = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
        return youtube_client

    def get_playlist_videos(self):
        #keep track of what page of the playlist we are on
        nextPageToken = None

        #loop over each page of the playlist so we are able to get all possible songs
        while True:
            pl_request = self.youtube_client.playlistItems().list(
                part = 'contentDetails',
                playlistId = "INSERT ANY PUBLIC YOUTUBE SONG PLAYLIST ID",
                maxResults = 50,
                pageToken = nextPageToken
            )

            pl_response = pl_request.execute()

            #grab the ids of the videos in the playlist
            vid_ids = []
            for item in pl_response['items']:
                vid_ids.append(item['contentDetails']['videoId'])

            vid_request = self.youtube_client.videos().list(
                part = 'snippet,contentDetails,statistics',
                id = ','.join(vid_ids)
            )

            vid_response = vid_request.execute()

            #collect each video/song and get its information
            for item in vid_response["items"]:
                video_title = item['snippet']['title']
                youtube_url = "https://www.youtube.com/watch?v={}".format(
                    item["id"])

                # use youtube_dl to collect the song name & artist name
                video = youtube_dl.YoutubeDL({}).extract_info(
                    youtube_url, download=False)
                song_name = video["track"]
                artist = video["artist"]
                print(artist)
                print(song_name)

                if song_name is not None and artist is not None:
                    # save all important info and skip any missing song and artist

                    self.all_song_info[video_title] = {
                        "youtube_url": youtube_url,
                        "song_name": song_name,
                        "artist": artist,

                        # add the uri, easy to get song to put into playlist
                        "spotify_uri": self.get_spotify_uri(song_name, artist)
                    }


            nextPageToken = pl_response.get('nextPageToken')

            if not nextPageToken:
                break


    def get_spotify_uri(self, song_name, artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        if songs:
            uri = songs[0]["uri"]
            return uri

    def add_song_to_playlist(self):
        """Add all liked songs into a new Spotify playlist"""
        # populate dictionary with our liked songs
        self.get_playlist_videos()

        # collect all of uri
        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]

        # filter out blank results from the uris
        res = list(filter(None, uris))

        # create a new playlist
        playlist_id = self.create_playlist()

        # add all songs into new playlist
        request_data = json.dumps(res)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code > 204:
            raise ResponseException(response.status_code)


        response_json = response.json()
        return response_json

    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Youtube Playlist",
            "description": "Youtube video playlist",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]


if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()
