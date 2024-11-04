import urllib.request
import json
with urllib.request.urlopen("https://api.watchmode.com/v1/title/345534/details/?apiKey=YOUR_API_KEY") as url:
    data = json.loads(url.read().decode())
    print(data)

{
  "id": 3173903,
  "title": "Breaking Bad",
  "original_title": "Breaking Bad",
  "plot_overview": "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
  "type": "tv_series",
  "runtime_minutes": 45,
  "year": 2008,
  "end_year": 2013,
  "release_date": "2008-01-20",
  "imdb_id": "tt0903747",
  "tmdb_id": 1396,
  "tmdb_type": "tv",
  "genres": [7],
  "genre_names": ["Drama"],
  "user_rating": 9.2,
  "critic_score": 85,
  "us_rating": "TV-MA",
}