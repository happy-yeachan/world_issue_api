import requests
from bs4 import BeautifulSoup
from papago import *
import re
def news_scraping(url_address,second_url_address,title_path,img_path,url_path,country_name,is_korea):
    try:
        url = url_address
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.select_one(title_path).text
        img = soup.select_one(img_path)['src']
        if country_name=='영국' or country_name=='베트남':
            url = second_url_address
            url +=  soup.select_one(url_path)['href']   
        else:
            url =  soup.select_one(url_path)['href']
        title = re.sub(r"^\s+|\s+$", "", title)
        if not is_korea:
            title = get_translate(str(title))

        result = {
            'country': country_name,
            'title': title,
            'img': img,
            'url': second_url_address + url
        }
        return result
    except:
        print('error:',end='')
        print(country_name)