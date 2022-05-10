import requests

response = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=0d370cc7d00efda0e60c03ccd6f6ad89&user_id=195573215%40N02&format=json&nojsoncallback=1")

print(response.json())
print(response.status_code)
