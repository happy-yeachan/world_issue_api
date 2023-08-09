import requests
from bs4 import BeautifulSoup
from papago import *
import re
from gpt import *

def news_scraping(url_address,second_url_address,title_path,img_path,url_path,country_name,is_korea,content_path):
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
            'url': second_url_address + url,        
        }
        #url 주소가 덧붙여서 나오는 나라들임, 그 때 그 떄 마다 다를 수 있어서 수정필요
        if country_name=='인도' or country_name=='프랑스' or country_name=='이탈리아' or country_name=='대한민국' or country_name=='영국' or country_name=='베트남':
            result['url']=url
        print(result['url'])
        content=content_scraping(result['url'],content_path)
        result['content']=content
        return result
    except Exception as ex:            
        print('error:',end='')
        print(country_name)    
        print(ex)

def content_scraping(url,content_path):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')    
    content = soup.select_one(content_path).text
    content = gpt(content)
    return content