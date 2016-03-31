import requests
import lxml
from lxml import html
import pandas as pd

components = {
    'food' : ['food', 'burger', 'fries', 'shake', 'eats'],
    'atmosphere' : ['atmosphere', 'ambience', 'place', 'vibe', 'feel'],
    'service' : ['service', 'server', 'waiter', 'cashier', 'waitress', 'worker', 'staff'],
    'wait' : ['wait', 'line', 'queue', 'time'],
}

url = "http://www.yelp.com/biz/hopdoddy-burger-bar-austin?osq=Hopdoddy+Burger+Bar"
component = 'wait'
first_url = url + "1?period=all"

def request_xml(url):
    response = requests.get(url)
    xml = html.fromstring(response.text)
    return xml

def find_end(self, xml):
    num_reviews = int (xml.xpath("//div/div[@class='results']/text()")[0]
        .split(' ')[0].split('(')[1])
    if num_reviews / 20 > 25 :
        pages = 26
    else :
        pages = num_reviews / 20
    return pages


xml = request_xml(first_url)
pages = find_end(xml)
