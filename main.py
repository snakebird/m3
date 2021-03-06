import requests

url = 'https://raw.githubusercontent.com/TheSamsungFreak/Filmy_PL_M3U/main/Hejo_TV.m3u'

myfile = requests.get(url)

print(myfile.text)

