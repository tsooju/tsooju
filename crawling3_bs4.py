# crawling3_bs4.py
# 네이버 영화 검색 순위 크롤링 분서 테스트

import urllib.request, bs4

web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
result_code = bs4.BeautifulSoup(web_page, "html.parser")


# 상영 영화정보 기록된 태그 엘리먼트 찾기
# 하나의 태그 엘리먼트는 find()
# find 는(찾을 순위 값이 기록된 상위태그명, html 태그속성="속성값")
# find(태그명)
# find_info = result_code.find("ul", class_="lst_detail_t1")
find_info = result_code.find(class_="lst_detail_t1")
print(find_info) #class 속성에 해당하는 ul 태그 정보 추출 


# 영화 목록별로 추출 : ul > li 
# 태그 앨리먼 여러 개 추출 : fidn_all()
movie_list=find_info.find_all("li")
print(len(movie_list))  # 추출한 li 태그

# 각 엘리먼트 안의 필요한 값들을 찾아냄
for idx in range(0, len(movie_list)):
    # 영화제목 찾아내기 작업
    movie_title = movie_list[idx].find(class_="tit").find("a").text
    print((idx + 1), '위 : ', movie_title)