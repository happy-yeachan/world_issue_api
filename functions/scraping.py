from datetime import datetime
import requests
import country_info
import func

#신규 나라 추가 코드 예시
# requests.post("http://223.130.139.67:8000/Issue/", json=Vietnam()) 
country=[]
for c_info in country_info.country_infos:  
    country.append(
        func.news_scraping(
            c_info['url'],
            c_info['plus_url'],
            c_info['title_path'],
            c_info['img_path'],
            c_info['article_url'],
            c_info['country_name'],
            c_info['is_korea'],
            c_info['article_path'],
        )
    )


# 조회수 0으로 초기화와 동시에 기사 내용 최신화
for i in range(len(country)):
    print(datetime.today().strftime("%Y-%m-%d %H:%M") )
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", country[i])
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", {
        "visite_count":0,
        "created_at":datetime.today().strftime("%Y-%m-%d %H:%M") 
    })

# requests.post("http://223.130.139.67:8000/Issue/", json=Brazil())