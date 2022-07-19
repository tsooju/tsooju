# crawling6_bs4.py

# 네이버 영화 상영정보 제공 페이지에서
# 상영순위, 제목, 평점, 관람가능나이를 추출해서
# Movie 클래스에 대한 객체(instance)에 저장한 다음에
# 각객체를 데이터베이스 movie 테이블에 저장한(insert) 다음
# select 조회로 출력 확인

import urllib.request, bs4
import Movie as mv
import common.oracle_db as oradb


# oracle 드라이버 등록 지정
oradb.oracle_init()

conn = ""
cursor = ""

query = "insert into movie values (:1, :2, :3, :4)"
try:
    web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
    result_code = bs4.BeautifulSoup(web_page, "html.parser")



    find_info = result_code.find(class_="lst_detail_t1")
    movie_list=find_info.find_all("li")


    conn = oradb.connect()
    cursor = conn.cursor()




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
        instance_list = []
        ref = mv.Movie(movie_title, star_point, age_grade, rank)
        print(ref)

        #쿼리문 반영 : 튜플 만들기
        tp_value = (rank, movie_title, star_point, age_grade)
        cursor.execute(query, tp_value)
        oradb.commit(conn)

    # db 에 기록 저장 끝============================================================

    # 저장 확인을 위해 db에서 select 조회해서 출력 처리

    resultset = cursor.execute("select * from movie").fetch_all()

    for row in resultset: # 리스트에서 객체 하나씩 꺼냄
        print(row)    # 행 단위로 출력

except Exception as msg:
    oradb.rollback(conn)
    print("네이버 영화 크롤링 분석 관력 에러 : ", msg)
finally:
    cursor.close()
    oradb.close(conn)
