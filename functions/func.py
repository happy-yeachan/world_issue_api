import requests
from bs4 import BeautifulSoup
from papago import *
import re
# from gpt import *

def news_scraping(url_address,second_url_address,title_path,img_path,url_path,country_name,is_korea,content_path):    
    try:
        url = url_address
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.select_one(title_path).text
        if country_name=='캐나다' or country_name=='네덜란드':
            img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png/692px-%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png'
        else:
            img = soup.select_one(img_path)['src']
        if country_name=='인도' or country_name=='멕시코' or country_name=='인도네시아' or country_name=='네덜란드':
            img=second_url_address+img
        if country_name=='영국' or country_name=='베트남':
            url = second_url_address
            url +=  soup.select_one(url_path)['href']               
        else:
            url =  soup.select_one(url_path)['href']
            print(country_name,url)
        title = re.sub(r"^\s+|\s+$", "", title)
        if not is_korea:
            title = get_translate(str(title))
        img_status = requests.get(img)
        if not img_status.status_code == 200:
            img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png/692px-%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png'
        result = {
            'country': country_name,
            'title': title,
            'img': img,
            'url': second_url_address + url,        
        }
        #url 주소가 덧붙여서 나오는 나라들임, 그 때 그 떄 마다 다를 수 있어서 수정필요
        if country_name=='필리핀' or  country_name=='러시아'or country_name=='인도'  or country_name=='프랑스' or country_name=='독일' or country_name=='이탈리아' or country_name=='대한민국' or country_name=='영국' or country_name=='베트남' or country_name=='스페인' or country_name=='멕시코' or country_name=='베트남':
            result['url']=url
        print(result['url'])
        content=content_scraping(result['url'],content_path)
        result['content']=content        
    except Exception as ex:
        print('error:', end='')
        print(country_name)
        print(ex)
        result = {
            'country': country_name,
            'title': 'error',
            'img': 'https://img.joongang.co.kr/svcimg/1000/index/202308/25183618_327_20230809192920.jpg/_ir_586x319_/',
            'url': 'https://www.joongang.co.kr/article/25183618',        
        }
        result['content']='error' 
    return result

def content_scraping(url,content_path):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')    
    content = soup.select_one(content_path).text
    # content = gpt(content)
    return content