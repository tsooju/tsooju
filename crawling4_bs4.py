# crawling4_bs4.py
# 실습 1 :
# 영화 상영작 정보 페이지에서 전체관람가, 15세관람가, 12세 관람가로
# 영화를 분류해서 각각 리스트에 저장한 다음 출력확인
# 전체관람가 리스트, 15세 관람가 리스트, 12세관람가 리스트
# 각 리스트에 저장 정보 예 : '1위 : 토르, 예매율 : 35%'

import urllib.request, bs4

web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
result_code = bs4.BeautifulSoup(web_page, "html.parser")


find_info = result_code.find(class_="lst_detail_t1")
movie_list = find_info.find_all("li")

list_12 = []
list_14 = []
list_all = []

for idx in range(0, len(movie_list)):
    movie_list[idx].find(class_="tit").find("a").text




    print(list_12.append(find_info))

# list_12 = []
# print(len(list_12))
# for idx in range(0, len(list_12)):
#     # 영화제목 찾아내기 작업
#     movie_title = movie_list[idx].find_all(class_="ico_rating_12")
#     print(list_12.append((idx + 1), '위 : ', movie_title))


