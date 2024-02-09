import requests

response = requests.get("https://api.deezer.com/playlist/9974949442/tracks")
tracklist_json = response.json()
tracklist_json = tracklist_json["data"]

# gets the first item
print(tracklist_json[0])