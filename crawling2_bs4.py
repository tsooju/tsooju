# crawling2_bs4.py
# url을 키보드로 입력답아서 크롤링 테스트

import urllib.request, bs4

url = input("접속할 페이지 url 을 입력하세요 :")
# url은 웹 상의 자원까지의 경로를 의미함.
# 프로토콜 ://도메인명/폴더명/파일명?이름=값&이름=값
# 쿼리스트링 : 서버측 대상 코드파일로 전달되는 값들을 표현한 것
#            ?이름=값&이름=값
# https://n.news.naver.com/article/022/0003712709?cds=news_media_pc&type=editn

web_page = urllib.request.urlopen(url)
result_code = bs4.BeautifulSoup(web_page, "html.parser")
print(result_code)