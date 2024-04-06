import pandas as pd
import re
import time
from nltk.corpus import stopwords as nltk_stopwords
import nltk

# Функции для предобработки текста
def clear_text(text):
    text = re.sub(r'[^А-яЁё]+', ' ', text).lower()
    return " ".join(text.split())

def clean_stop_words(text, stopwords):
    text = [word for word in text.split() if word not in stopwords]
    return " ".join(text)

# Загрузка стоп-слов
nltk.download('stopwords')
stopwords = set(nltk_stopwords.words('russian'))

# Пути к исходным данным
positive_tweets_path = r"F:\SentimentAnalysis\data\community_datasets\mokoron_raw_dataset\positive.csv"
negative_tweets_path = r"F:\SentimentAnalysis\data\community_datasets\mokoron_raw_dataset\negative.csv"

# Загрузка данных
positive_tweets = pd.read_csv(positive_tweets_path, sep=',', header=None)
negative_tweets = pd.read_csv(negative_tweets_path, sep=',', header=None)

# Обработка данных и присвоение меток
positive_text = positive_tweets.iloc[:, 3].to_frame('text')
positive_text['label'] = 1

negative_text = negative_tweets.iloc[:, 3].to_frame('text')
negative_text['label'] = 0

# Объединение положительных и отрицательных твитов в один датафрейм
labeled_tweets = pd.concat([positive_text, negative_text], ignore_index=True)

# Очистка текстов
start_clean = time.time()
labeled_tweets['text_clear'] = labeled_tweets['text'].apply(lambda x: clean_stop_words(clear_text(str(x)), stopwords))
print('Обработка текстов заняла: '+str(round(time.time() - start_clean, 2))+' секунд')

# Сохранение обработанных данных
output_path = r"F:\SentimentAnalysis\data\clean_dataset\labeled_tweets.csv"
labeled_tweets.to_csv(output_path, index=False, encoding='utf-8')

# Проверка результатов
print(labeled_tweets.head())
