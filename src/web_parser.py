import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import pandas as pd

# Зададим путь к основной папке
path_main = r"F:\SentimentAnalysis\data\reviews"

# Зададим путь к папке с драйвером Edge
path_edge_driver = r"F:\SentimentAnalysis\selenium_driver\msedgedriver.exe"

# Список для собранных комментариев
scrapped = []

with webdriver.Edge(service=Service(path_edge_driver)) as driver:
    wait = WebDriverWait(driver, 20)
    driver.get("ССылка на ресурс") # Ссылка на необходимый ресурс

    # Прокрутка страницы для загрузки комментариев
    for item in tqdm(range(200)):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(2.5)

    # Сбор комментариев
    comments_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content")))
    for element in comments_elements:
        scrapped.append(element.text)

# Обработка собранных комментариев
comments_processed = [x.split('\nОТВЕТИТЬ')[0].split('\n') for x in scrapped[0].split('назад')]
comments_final = [x[1] for x in comments_processed if len(x) > 1][2:] + scrapped[1:]

# Создание DataFrame и сохранение в CSV
comments_df = pd.DataFrame({'comment': comments_final})
comments_df.to_csv(path_main + '\\comments.csv', index=False, encoding='utf-8')

# Вывод первых нескольких строк DataFrame для проверки
print(comments_df.head())