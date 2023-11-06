import requests

response = requests.get("https://api.deezer.com/playlist/9974949442/tracks")
print(response.json())