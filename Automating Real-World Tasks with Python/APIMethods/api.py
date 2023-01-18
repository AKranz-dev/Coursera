#GET Request
 import requests
 response = requests.get('https://www.google.com')

#Print the first 300 characters of the response
 print(response.text[:300])
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9


#Print the raw, uncompressed response:
 response = requests.get('https://www.google.com', stream=True)
 print(response.raw.read()[:100])
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'


#Attatching parameters to a GET request
 p = {"search": "grey kitten",
      "max_results": 15}
 response = requests.get("https://example.com/path/to/api", params=p)
 response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'


#Attatching data to a POST request
 p = {"description": "white kitten",
      "name": "Snowball",
      "age_months": 6}
 response = requests.post("https://example.com/path/to/api", data=p)


#Formatting POST request data into JSON using the json parameter where p is a Python dictionary of data about a kitten
 response = requests.post("https://example.com/path/to/api", json=p)
 response.request.url
'https://example.com/path/to/api'
 response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 