import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

currunt_folder = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(currunt_folder, 'chromedriver.exe')

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://google.com')

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)
# time.sleep(3)

song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.button_icons.type03.song_info')

for i in range(5):
    song_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    # driver.find_element(By.CSS_SELECTOR, 'di.list').text
    song_meta = driver.find_element(By.CSS_SELECTOR, 'dl.list')

    for child in song_meta.find_elements(By.CSS_SELECTOR, 'dt, dd'):
        if child.tag_name == 'dt':
            print(child.text, end=':')
        else:
            print(child.text)

    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    print(like_cnt)

    driver.back()