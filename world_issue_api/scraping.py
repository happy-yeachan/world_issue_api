from datetime import datetime
import requests
import country_info

#신규 나라 추가 코드 예시
# requests.post("http://223.130.139.67:8000/Issue/", json=Vietnam()) 

country = country_info.country_infos

# 조회수 0으로 초기화와 동시에 기사 내용 최신화
for i in range(len(country)):
    print(datetime.today().strftime("%Y-%m-%d %H:%M") )
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", country[i])
    requests.patch("http://223.130.139.67:8000/Issue/" + str(i+1) + "/", {
        "visite_count":0,
        "created_at":datetime.today().strftime("%Y-%m-%d %H:%M") 
    })

# requests.post("http://223.130.139.67:8000/Issue/", json=Brazil())