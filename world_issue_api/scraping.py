
import requests
from bs4 import BeautifulSoup
from papago import *

def USA():
    url = 'https://edition.cnn.com/us'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2) > div > div > span').text
    img = soup.select_one('body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(1) > div > div > div.image__container.image > picture > img')['src']
    url =  soup.select_one('body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2)')['href']
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '미국',
        'title': title,
        'img': img,
        'url': 'https://edition.cnn.com' + url
    }
    return result


def Japan():
    url = 'https://mainichi.jp/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-detail > h3').text
    img = soup.select_one('#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-image.image-mask > picture > img')['src']
    url =  soup.select_one('#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '일본',
        'title': title,
        'img': img,
        'url': 'https://mainichi.jp'+ url
    }
    return result


def India():
    url = 'https://www.thequint.com/international'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link > div > h1').text
    img = soup.select_one('#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a:nth-child(1) > div > figure > picture > img')['src']
    url =  soup.select_one('#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '인도',
        'title': title,
        'img': img,
        'url': url
    }
    return result


def France():
    url = 'https://www.lemonde.fr/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > h1 > p').text
    img = soup.select_one('#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > div.article__media-container > picture > img')['src']
    url =  soup.select_one('#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '프랑스',
        'title': title,
        'img': img,
        'url': url
    }
    return result


import re
def Canada():
    url = 'https://www.thestar.com/news/canada/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a').text
    img = soup.select_one('#card-summary-3f9057df-e038-528c-ac9f-cc6f703bbc00 > div > div.card-image > div > figure > div > a > img')['src']
    url =  soup.select_one('#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '캐나다',
        'title': title,
        'img': img,
        'url': 'https://www.thestar.com/news/canada'+url
    }
    return result


# def Rusia():
#     url = 'https://iz.ru/'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
    
#     title = soup.select_one('#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top')
#     img = soup.select_one('#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top')
#     url =  soup.select_one('#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top > a')  
#     title = get_translate(str(title))

#     result = {
#         'country': '러시아',
#         'title': title,
#         'img': img,
#         'url': url
#     }
#     json_val = json.dumps(result, ensure_ascii=False)
#     return str(json_val)

def Germany():
    url = 'https://www.faz.net/aktuell/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img=url
    title = soup.select_one('#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a > header > h2 > span.tsr-Base_HeadlineText').text
    img = soup.select_one('#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.tsr-Base_MediaWrapper.btn-Wrapper > img')['src']
    url =  soup.select_one('#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a')['href']
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '독일',
        'title': title,
        'img': img,
        'url': url
    }
    return result



def UK():
    url = 'https://www.bbc.com/news/uk'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a').text
    img = soup.select_one('#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-image.gs-u-mb.gs-u-mb0\@xs.gel-2\/3\@m.gel-1\/2\@xl > div > div > img')['src']
    url = 'https://www.bbc.com'
    url +=  soup.select_one('#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '영국',
        'title': title,
        'img': img,
        'url': url
    }
    return result


def Italy():
    url = 'https://www.repubblica.it/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)').text
    img = soup.select_one('#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > figure > a > picture > img')['src']    
    url =  soup.select_one('#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)
    title = get_translate(str(title))

    result = {
        'country': '이탈리아',
        'title': title,
        'img': img,
        'url': url
    }
    return result


def Brazil():
    url = 'https://www.uol.com.br/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#lkj543zr').text    
    img = soup.select_one('#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a > figure > picture > img')['src']    
    url =  soup.select_one('#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a')['href']       
    title = re.sub(r"^\s+|\s+$", "", title)
    # title = get_translate(str(title))

    result = {
        'country': '브라질',
        'title': title,
        'img': img,
        'url': url
    }
    
    return result


def Korea():
    url = 'https://www.joongang.co.kr/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.select_one('#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > div > h2 > a').text
    img = soup.select_one('#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > figure > a > img')['src']
    url =  soup.select_one('#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > div > h2 > a')['href']   
    title = re.sub(r"^\s+|\s+$", "", title)

    result = {
        'country': '대한민국',
        'title': title,
        'img': img,
        'url': url
    }
    return result


from datetime import datetime
country = [USA(), Japan(), India(), France(), Germany(), UK(), Italy(), Korea()]
#Canada()  Brazil() 추가예정

for i in range(len(country)):
    print(i)
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", json=country[i])
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", {
        "visite_count":0,
        "created_at":datetime.today().strftime("%Y%m%d") 
    })
