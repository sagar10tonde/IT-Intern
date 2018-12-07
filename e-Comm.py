import requests
import csv
from bs4 import BeautifulSoup

def get_product_info1(source):
    info = {}
    all_tr = source.find_all('tr')
    for tr in all_tr:
        tr_key = tr.findAll('td')[0].text
        tr_val = tr.findAll('td')[1].text
        info[tr_key] = tr_val


    return info

def get_product_info(source,url):
    global all_li
    info = []

    if 'amazon.in' in url:
        all_li = source.find_all('li')
        for li in all_li:
            info.append(li.find('span').text.strip())
        return info

    elif 'flipkart.com' in url:
        for li in source:
            all_li = li.findAll('li')
        for li in all_li:
            info.append(li.text.strip())
        return info

    elif 'snapdeal.com' in url:
        all_li = source.findAll('span' , attrs = {"class": "h-content"})
        for li in all_li:
            info.append(li.text.strip())
        return info

def get_info_flipkart(soup, url):
    data = []
    name = soup.find_all("span", attrs={"class": "_35KyD6"})[0].text.strip()
    price = soup.find_all("div", attrs={"class": "_1vC4OE _3qQ9m1"})[0].text.strip()
    info = get_product_info(soup.find_all("div", attrs={"class": "_3WHvuP"}),url)
    data.append(name)
    data.append('flipkart.com')
    data.append(price)
    data.append(info)
    data.append(url)

    return data

def get_info_amazon(soup,url):
    data = []
    name = soup.find('span', {'class': 'a-size-large'}).text.strip()
    price = soup.find('span', {'class': 'a-size-medium a-color-price'}).text.strip()
    #info = get_product_info(soup.find('div', {'class': 'content pdClearfix'}))
    info = get_product_info(soup.find('div', {'class': 'a-section a-spacing-medium a-spacing-top-small'}),url)
    data.append(name)
    data.append('amazon.in')
    data.append(price)
    data.append(info)
    data.append(url)

    return data

def get_info_snapdeal(soup,url):
    data = []
    name = soup.find('h1', {'class': 'pdp-e-i-head'}).text.strip()
    price = soup.find('span', {'class': 'payBlkBig'}).text.strip()
    info = get_product_info(soup.find('div', {'class': 'spec-body p-keyfeatures'}), url)
    data.append(name)
    data.append('snapdeal.com')
    data.append(price)
    data.append(info)
    data.append(url)

    return data


def for_multi_url():
    fp = open('input-e-Comm.txt', "r")
    urlList = fp.readlines()
    fp.close()

    for url in urlList:
        url=url.strip("\n")
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')

        if 'flipkart.com' in url:
            data = get_info_flipkart(soup, url)
            with open('output.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data)

        elif 'amazon.in' in url:
            data = get_info_amazon(soup, url)
            with open('output.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data)

        elif 'snapdeal.com' in url:
            data = get_info_snapdeal(soup, url)
            with open('output.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data)


def for_one_url(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    if 'amazon.in' in url:
        data = get_info_amazon(soup, url)
        with open('output.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    elif 'flipkart.com' in url:
        data = get_info_flipkart(soup, url)
        with open('output.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    elif 'snapdeal.com' in url:
        data = get_info_snapdeal(soup, url)
        with open('output.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)



url1 = 'https://www.flipkart.com/mi-max-2-black-64-gb/p/itmevkftufr4d5e2'
url2 = 'https://www.amazon.in/dp/B073GTVVW7'
url3 = 'https://www.snapdeal.com/product/intex-blue-aqua-star-i10/5188147452280046171'
#for_one_url(url3)
for_multi_url()
