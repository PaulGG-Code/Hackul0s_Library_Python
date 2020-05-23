import requests, hashlib
from bs4 import BeautifulSoup

url = "http://docker.hackthebox.eu:31726/"

s = requests.session()
response = s.get(url)

soup = BeautifulSoup(response.content, "lxml")

str = soup.h3.string
hash = hashlib.md5(str.encode()).hexdigest()

myobj = {'hash': hash}

flag = s.post(url, data = myobj)

print(flag.text)
