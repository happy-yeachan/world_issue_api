import requests
from bs4 import BeautifulSoup
from papago import *
import re
# from gpt import *
import country_info

def news_scraping(url_address,second_url_address,title_path,img_path,url_path,country_name,is_korea,content_path):    
    try:
        url = url_address
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.select_one(title_path).text
        #이미지 url이 request 했을 때 error를 유발하는 나라들은 고정 이미지를 할당
        if country_name=='캐나다' or country_name=='네덜란드':
            img = country_info.lion_img
        else:
            img = soup.select_one(img_path)['src']
        #tmg url이 상대경로인 경우의 나라
        if country_name=='인도' or country_name=='멕시코' or country_name=='인도네시아' or country_name=='네덜란드':
            img=second_url_address+img
        #a태그의 url이 상대경로인 나라
        if country_name=='영국' or country_name=='베트남':
            url = second_url_address
            url +=  soup.select_one(url_path)['href']               
        else:
            url =  soup.select_one(url_path)['href']
        title = re.sub(r"^\s+|\s+$", "", title)
        if not is_korea:
            title = get_translate(str(title))
        #img를 불러올 수 있는지 확인하기 위에 get요청을 보냄
        img_status = requests.get(img)
        #img를 불러오지 못했다면 고정 이미지를 할당
        if not img_status.status_code == 200:
            img = country_info.lion_img
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
    #에러 날 시 title을 error로 지정하고 img와 url은 대한민국의 중앙일보로 넣는다.(형식을 맞춰 오류가 안나게 하기 위함 아무거나 상관 x)        
    except Exception as ex:
        print('error:', end='')
        print(country_name)
        print(ex)
        result = {
            'country': country_name,
            'title': 'Not-Found',
            'img': country_info.lion_img,
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