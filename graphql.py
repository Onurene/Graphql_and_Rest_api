import requests
import json

graphql_url = "http://localhost:4000/graphql"


class Solution:
    def get_response(self, url, query):
        response = requests.get(url=url, json={"query": query})
        print("response status code: ", response.status_code)
        if response.status_code == 200:
            #print("response : ", response.content)
            response_str = response.content.decode('utf-8')
            data = json.loads(response_str)
            return data 
    
    def get_albums(self):
        query = """
                query { 
                    artists(where: {name: "Red Hot Chili Peppers"}) 
                    { 
                        albums{ 
                            title 
                            } 
                    } 
                    }
                """
        data = self.get_response(graphql_url,query)
        titles = [album['title'] for album in data['data']['artists'][0]['albums']]
        print("Albums by the artist Red Hot Chili Peppers is: ")
        print(titles,'\n')
        return
    
    def get_genres(self):
        query = """
            query {
                artists(where: {name: "U2"}){
                    albums {
                        tracks {
                            genre {
                            name
                            }
                        }
                    }
                }
            }
        """
        data = self.get_response(graphql_url,query)
        unique_genres = set()
        for artist in data["data"]["artists"]:
            for album in artist["albums"]:
                for track in album["tracks"]:
                    genre_name = track["genre"]["name"]
                    unique_genres.add(genre_name)
        print("Genres associated with the artist U2 are: ")
        print(list(unique_genres),'\n')
        return

    def get_track_info(self):
        query = """
                    query {
                        playlists(where: {name: "Grunge"}) {
                            name
                                tracks {
                                    name
                                    album {
                                        title
                                        artist {
                                            name
                                        }
                                    }
                                }
                            }
                        }
                    """
        
        data = self.get_response(graphql_url,query)
        playlist_data = data["data"]["playlists"][0]

        # Iterate through tracks and format the output
        output_lines = []
        for track in playlist_data["tracks"]:
            track_name = track["name"]
            artist_name = track["album"]["artist"]["name"]
            album_title = track["album"]["title"]
            
            output_lines.append(f"{track_name} | {artist_name} | {album_title}")

        # Join the formatted lines into a single string
        print("Tracks | Artists | Albums")
        formatted_output = "\n".join(output_lines)

        # Print the formatted output
        print(formatted_output,'\n')
        return

s = Solution()
s.get_albums()
s.get_genres()
s.get_track_info()