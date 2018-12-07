import requests
from json import dump
from bs4 import BeautifulSoup
from pprint import pprint

#urls = "https://en.wikipedia.org/wiki/Tango_Charlie"
#urls = "https://en.wikipedia.org/wiki/Akshay_Kumar"
urls = "https://en.wikipedia.org/wiki/Pune"
#urls = "https://en.wikipedia.org/wiki/Narendra_Modi"

def get_values(values):
    new = []
    for i in list(values):
        if len(ascii(i)) >= 4:
            pass
        else:
            new.append(i)

    return "".join(new)

def get_keys(keys):
    skey1 = ['(','{','[']
    keys2 = keys
    keys3 = ""
    if len(ascii(list(keys)[0])) >= 4:
        keys2 = "".join(list(keys)[2:])

    keys2 = keys2.replace(" ","_")

    for i in range(len(keys2)):
        if keys2[i] in skey1:
            return keys3
        else:
            keys3+=keys2[i]

    return keys3

def findInfo(url):

    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    data = {}
    file_name = (url.split('/')[-1]+".json").lower()

    divs = soup.findAll("table", {"class": "infobox"})
    for div in divs:
        rows = div.findAll("th", {"scope": "row"})
        for row in rows:
            key = get_keys((row.text).lower().strip())
            values = get_values(row.find_next_sibling("td").text.strip())
            data[key] = values


    with open(file_name, "w+") as fp:
        dump(data,fp)
    fp.close()

    pprint(data)


findInfo(urls)
