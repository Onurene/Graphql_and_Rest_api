import requests
import json

rest_url = "http://localhost:8000/api/tables"

class Solution:
    def get_albums(self):
        artist_name = "Red Hot Chili Peppers"
        response = requests.get(f"{rest_url}/artists/rows?_schema=artistid&_filters=Name:{artist_name}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)
        artist_id = data['data'][0]['ArtistId']
        response = requests.get(f"{rest_url}/albums/rows?_schema=title&_filters=artistid:{artist_id}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)
        titles = [album['Title'] for album in data['data']]
        print("Albums by the artist Red Hot Chili Peppers is: ")
        print(titles,'\n')
        return
    
    # Genres associated with the artist “U2.”
    def get_genres(self):
        artist_name = "U2"
        response = requests.get(f"{rest_url}/artists/rows?_schema=artistid&_filters=Name:{artist_name}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)
        artist_id = data['data'][0]['ArtistId']
        response = requests.get(f"{rest_url}/albums/rows?_schema=albumid&_filters=artistid:{artist_id}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)
        album_ids = [item['AlbumId'] for item in data['data']]

        genre_id = set()
        for i in album_ids:
            response = requests.get(f"{rest_url}/tracks/rows?_schema=genreid&_filters=albumid:{i}")
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)    
            result = data['data'][0]['GenreId']
            genre_id.add(result)

        genre_result = []
        for i in genre_id:
            response = requests.get(f"{rest_url}/genres/rows?_schema=name&_filters=genreid:{i}")
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)  
            genre_result.append(data['data'][0]['Name'])
        print("Genres associated with the artist U2 are: ")
        print(genre_result,'\n')
        return

    # Names of tracks on the playlist “Grunge” and their associated artists and albums.
    def get_track_info(self):
        name = "Grunge"
        response = requests.get(f"{rest_url}/playlists/rows?_schema=playlistid&_filters=name:{name}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)  
        playlist_id = data['data'][0]['PlaylistId']
        response = requests.get(f"{rest_url}/playlist_track/rows?_limit=50&_schema=trackid&_filters=playlistid:{playlist_id}")
        response_str = response.content.decode('utf-8')
        data = json.loads(response_str)  
        track_ids = [item['TrackId'] for item in data['data']]

        album_ids = []
        track_names = []
        for id in track_ids:
            response = requests.get(f"{rest_url}/tracks/rows?&_schema=albumid,name&_filters=trackid:{id}")
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)  
            album_ids.append(data['data'][0]['AlbumId'])
            track_names.append(data['data'][0]['Name'])

        artist_ids = []
        albums = []
        for id in album_ids:
            response = requests.get(f"{rest_url}/albums/rows?&_schema=artistid,title&_filters=albumid:{id}")
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)  
            
            artist_ids.append(data['data'][0]['ArtistId'])
            albums.append(data['data'][0]['Title'])
        
        artist_name = []
        for id in artist_ids:
            response = requests.get(f"{rest_url}/artists/rows?&_schema=name&_filters=artistid:{id}")
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)
            artist_name.append(data['data'][0]['Name'])

        output_lines = []
        for i,j,k in zip(track_names,albums,artist_name):
            output_lines.append(f"{i} | {j} | {k}")
        
        print("Tracks | Artists | Albums")
        formatted_output = "\n".join(output_lines)
        # Print the formatted output
        print(formatted_output,'\n')
        return
    
s = Solution()
s.get_albums()
s.get_genres()
s.get_track_info()



