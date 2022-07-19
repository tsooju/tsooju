# crawling_bs4.py
# bs4(beautifulsoup4)를 이용한 웹 클로링 테스트 코드

# import bs4
# import urllib.request

import urllib.request, bs4
# urllib.request : 웹 상의 데이터를 가져오는 모듈이다.
# bs4는 웹 페이지의 웹문서 html로 분석하는 모듈이다.
# 해당 url 페이지에 접속함
web_page = urllib.request.urlopen("https://www.naver.com/")
# 접속한 페이지 소스를 읽어와서 출력
print(web_page.read())

# 읽어온 인코딩된 웹 코드를 html 태그로 바꿈
result_code = bs4.BeautifulSoup(web_page, "html.parser")
print(result_code)

