import urllib.request
import json
with urllib.request.urlopen("https://api.watchmode.com/v1/genres/?apiKey=YOUR_API_KEY") as url:
    data = json.loads(url.read().decode())
    print(data)


    [
  { "id": 4, "name": "Comedy", "tmdb_id": 35 },
  { "id": 6, "name": "Documentary", "tmdb_id": 99 },
  { "id": 33, "name": "Anime", "tmdb_id": null }
]