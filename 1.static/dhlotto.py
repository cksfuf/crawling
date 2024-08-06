import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.dhlottery.co.kr/common.do?method=main'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser') # 이쁘게 뽑아주는거임.
# print(soup)

# balls = soup.select('span.ball_645')
# for ball in balls:
#     print(ball)

# print(soup.select('span.bonus + span'))

# print(soup.select('a#numView')) a태그

print(soup.select('a[href*=/gameResult]')) # a태그 속성