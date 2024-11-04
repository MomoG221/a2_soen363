import urllib.request
import json
with urllib.request.urlopen("https://api.watchmode.com/v1/regions/?apiKey=YOUR_API_KEY") as url:
    data = json.loads(url.read().decode())
    print(data)

    [
  {
    "country": "US",
    "name": "USA",
    "flag": "https://cdn.watchmode.com/misc_images/icons/usFlag2.png",
    "data_tier": 1,
    "plan_enabled": true
  },
  {
    "country": "CA",
    "name": "Canada",
    "flag": "https://cdn.watchmode.com/misc_images/icons/flagCA.png",
    "data_tier": 1,
    "plan_enabled": true
  },
  {
    "country": "GB",
    "name": "Great Britain",
    "flag": "https://cdn.watchmode.com/misc_images/icons/flagGB.png",
    "data_tier": 1,
    "plan_enabled": true
  },
  {
    "country": "AU",
    "name": "Australia",
    "flag": "https://cdn.watchmode.com/misc_images/icons/flagAU.png",
    "data_tier": 1,
    "plan_enabled": true
  },
  {
    "country": "AR",
    "name": "Argentina",
    "flag": "https://cdn.watchmode.com/misc_images/icons/flagAR.png",
    "data_tier": 2,
    "plan_enabled": false
  },
  {
    "country": "BE",
    "name": "Belgium",
    "flag": "https://cdn.watchmode.com/misc_images/icons/flagBE.png",
    "data_tier": 2,
    "plan_enabled": false
  }
]