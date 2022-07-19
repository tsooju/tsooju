# Movie.py
# 크롤링한 영화 정보 저장용 객체를 위한 클래스 정의 스크립트

class Movie:
    # 멤버변수(field) : private 적용
    __title = ""        # 영화제목 저장용 필드
    __star_point = 0    # 평점
    __age_grade = ""     # 관람가능 제한 나이
    __rank = 0          # 평점 순위

    # 생성자(constructor) : new 할 때 작동되는 함수 (만들자마자 초기화 하는 객체)
    def __init__(self, title, point, age, rank):
        self.__title = title
        self.__star_point = point
        self.__age_grade = age
        self.__rank = rank


    # 소멸자 생략
    # 멤버함수(method)
    # 연산자 오버로딩(overloading : 중복 정의)
    # __str__ : 자바의 toString() 메소드와 같음
    # __str__ : 객체가 가진 필드 값들을 하나의 문장(str)으로 만들어서 리턴함.
    def __str__(self):
        return "{}, {}점, {}세, 개봉순위 : {}위".format(self.__title, self.__star_point, self.__age_grade, self.__rank)