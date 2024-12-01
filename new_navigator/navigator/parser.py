import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from time import sleep

times = []
teachers = []
subs = []
urls = []
cabinets = []
day_format = []

driver = webdriver.Chrome()
driver.get("https://airtable.com/appcJGGcLssocnsot/shrqCWkSykpS7PJ6Y/tblk1iBDpqhztUBO8")
scroll_global = 0


def scroll_down():
    view_container = driver.find_element(By.CLASS_NAME, 'light-scrollbar')
    c_h = driver.execute_script("arguments[0].scrollTop += 100; return arguments[0].scrollTop;", view_container)
    return c_h


try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#viewContainer"))
    )
    day_of_week = driver.find_element(By.CLASS_NAME, 'top-bar-text-light-primary-hover-forced').text
    print(day_of_week)
    while True:
        elements = driver.find_elements(By.CLASS_NAME, 'cellContainer')

        count = 1
        for element in elements:
            if 4 < len(element.text) <= 50 and element.text[0].isupper() and element.text.count(
                    '.') == 0:
                subs.append(element.text)
            elif re.match(r'^[0-9]{1,2}:[0-9]{1,2}', element.text):
                times.append(element.text)

            elif element.text.count('.') == 2 and re.match(r'^[А-Я]{1}', element.text):
                teachers.append(element.text)

            elif re.match(r'^[0-9]{3}', element.text) or element.text == 'вирт.каб.':
                cabinets.append(element.text)

            elif re.match(r'^http', element.text):
                urls.append(element.text)

            elif re.match(r'^[а-я]{1}$', element.text):
                day_format.append(element.text)

            elif element.text != '':
                count += 1

        a1 = scroll_down()
        if scroll_global == a1:
            break
        scroll_global = a1
        # if len(driver.find_elements(By.CLASS_NAME, 'truncate-block-4-lines')) <= 6:
        #     break
finally:
    driver.quit()

subjects = {}

for i in range(len(times)):
    if not times[i] in subjects:
        subjects[times[i]] = [teachers[i], subs[i], urls[i], cabinets[i], day_format[i]]
result = {'class': day_of_week.split('_')[0], 'week': day_of_week.split('_')[1], 'subjects': subjects}
s = json.dumps(result)

open('../json/data.json', 'w').write(s)
