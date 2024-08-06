import os
import csv
import json
import requests
from dotenv import load_dotenv

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')

# print(KOBIS_API_KEY)

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

# WEKLY_URL = f'{URL}?key=??&targetDt=??' 형식
WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'

# print(WEEKLY_URL)

res = requests.get(WEEKLY_URL)
data = res.json() # 제이슨 구조인 res를 딕셔너리 구조로 조정해준거임. 파이썬에서 출력하기 위한 과정
# print(data)

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']


movie_dict = {} # 딕셔너리 구조로 저장해보기

for movie in movie_list:
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수': movie['audiAcc'],
    }

# movie_dict를 ./data/weekly.json 저장
output_dir = './data'
output_file = os.path.join(output_dir, 'weekly.json')


# 딕셔너리를 제이슨으로 바꾸기
if not os.path.exists(output_dir): # 아웃풋 dir 이 없으면 dir 구조 만들어달라는 if 문
    os.makedirs(output_dir)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(movie_dict, f, ensure_ascii=False)
    # f = open 이 뜻과 같음. with문이 끝나면 열린 파일을 닫아줌.


# movie_dict ./data/weekly.csv 저장
output_file = os.path.join(output_dir, 'weekly.csv')

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['대표코드', '영화명', '누적관객수'])
    for movie in movie_list:
        csv_writer.writerow([movie['movieCd'], movie['movieNm'], movie['audiAcc']])