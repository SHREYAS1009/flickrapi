#key
#600fe7c16227548828a45b4e809f1f9b

#secret
#50c652d05c3ed6c2
import json
from urllib.request import urlopen
tag="cat"
url="https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=8d72e169921afe991e73691116133596&tags='tag'&format=json&nojsoncallback=1&api_sig=05c0e1d5d59246d1377ce60e4a5bdfc9"


print(urlopen(url).read())

print(json.load(url))