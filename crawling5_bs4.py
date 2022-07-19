# crawling5_bs4.py
# 네이버 영화 상영정보 제공 페이지에서
# 상영순위, 제목, 평점, 관람가능나이를 추출해서
# Movie 클래스에 대한 객체(instance)에 저장한 다음에
# 각객체를 리스트에 저장한 다음 출력 확인

import urllib.request, bs4
import Movie as mv
web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
result_code = bs4.BeautifulSoup(web_page, "html.parser")



find_info = result_code.find(class_="lst_detail_t1")
movie_list=find_info.find_all("li")




# 각 엘리먼트 안의 필요한 값들을 찾아냄
for idx in range(0, len(movie_list)):

    movie_title = movie_list[idx].find(class_="tit").find("a").text
    star_point = movie_list[idx].find("div", class_="star_t1")
    rank = idx + 1
    age_grade = ""
    if movie_list[idx].find(class_="tit").find("span", class_="ico_rating_12").find("a").text
        age_grade = "15"
    elif movie_list[idx].find(class_="tit").find("span", class_="ico_rating_15").find("a").text
        age_grade = "12"
    elif movie_list[idx].find(class_="tit").find("span", class_="ico_rating_15").find("a").text
        age_grade = "all"

    # movie 객체 생성하면서, 초기값 전달 기록 처리
    # 파이선 클래스 객체 생성 : 객체참조변수 = 모듈명.생성자(초기값)
    # 생성자 사용 : 클래스명과 생성자함수명 같음
    ref = mv.Movie(movie_title, star_point, age_grade, rank)
    instance_list.append(ref)  # 객체를 리스트에 추가

# 저장된 리스트정보 출력 처리
for movie in instance_list:    # 리스트에서 객체 하나씩 꺼냄
    print(movie)    # 객체 정보 출력 : __str__ 이 자동 실행됨.


