
# importing the requests library
import requests
  
# api-endpoint
URL = "https://www.dpcs.dj/TFBPCS/cusLogin/checkvessels/2100004839"
# URL = "https://www.dpcs.dj/TFBPCS/cusLogin/checkvessels/"
URL = "https://www.google.com"

r = requests.get(url=URL)
# extracting data in json format
# data = r.json()
# headers = r.headers()
# requests.post(URL, data=r.json.dumps(data))

# for i in dir(r):
#   print(i)

data = r.text

print(data)