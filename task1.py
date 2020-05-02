import json
import urllib
from bs4 import BeautifulSoup
import requests

# change the another search topic you like
search_topic = "art"

URL = "https://www.coursebuffet.com/search?q=" + search_topic
req = requests.get(URL, timeout=5)
raw_html = BeautifulSoup(req.content, "html.parser")

values = {'q':'basic'}

course_title = raw_html.find_all('span', {'class':{'resultlist-unit-coursetitle'}})
course_desc = raw_html.find_all('span', {"class":{"resultlist-unit-coursedesc"}})


Array = []

for cb in raw_html('li', attrs={"class": "resultlist-unit"}):
    Object = {
            "course_title": cb.find('span', {'class':{'resultlist-unit-coursetitle'}}).text.encode('utf-8'),
            "course_desc": cb.find('span', {'class':{'resultlist-unit-coursedesc'}}).text.encode('utf-8').replace("\n","")
    }
    Array.append(Object)


with open('result.json', 'w') as outfile:
    json.dump(Array, outfile)
