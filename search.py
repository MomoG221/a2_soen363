import urllib.request
import json
with urllib.request.urlopen("https://api.watchmode.com/v1/search/?apiKey=YOUR_API_KEY&search_field=name&search_value=Ed%20Wood") as url:
    data = json.loads(url.read().decode())
    print(data)

    {
  "title_results": [
    {
      "id": 1114888,
      "name": "Ed Wood",
      "type": "movie",
      "year": 1994,
      "imdb_id": "tt0109707",
      "tmdb_id": 522,
      "tmdb_type": "movie"
    }
  ],
  "people_results": [
    {
      "id": 710125611,
      "name": "Ed Wood",
      "main_profession": "cinematographer",
      "imdb_id": "nm7903892",
      "tmdb_id": 2901757
    }
  ]
}