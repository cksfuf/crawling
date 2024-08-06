import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'

# SEARCH_MOVIE_URL = f'{URL}?key={KOBIS_API_KEY}&movieCd=???' 형식
SEARCH_MOVIE_URL = f'{URL}?key={KOBIS_API_KEY}&movieCd='

input_dir = './data'
input_file = os.path.join(input_dir, 'weekly.json')

with open(input_file, 'r', encoding='utf-8') as f: # 제이슨 형식을 딕셔너리로 바꾸는 json.load()
    movie_dict = json.load(f)
    
    for movie_cd in movie_dict.keys():
        SM_URL = SEARCH_MOVIE_URL + movie_cd

        res = requests.get(SM_URL)
        data = res.json()

        actors = data['movieInfoResult']['movieInfo']['actors']
        actor_str = ', '.join([actor['peopleNm'] for actor in actors])
        print(actor_str)
