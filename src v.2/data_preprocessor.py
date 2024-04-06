import re
from nltk.corpus import stopwords as nltk_stopwords
from pymystem3 import Mystem

class DataPreprocessor:
    def __init__(self):
        self.mystem = Mystem()
        self.stopwords = set(nltk_stopwords.words('russian'))
    
    def clean_text(self, text):
        text = re.sub(r'[^а-яА-ЯёЁ]', ' ', text)
        return text
    
    def lemmatize(self, text):
        lemmatized = ''.join(self.mystem.lemmatize(text))
        return lemmatized
    
    def remove_stopwords(self, text):
        text = [word for word in text.split() if word not in self.stopwords]
        return ' '.join(text)
    
    def preprocess(self, text):
        text = self.clean_text(text)
        text = self.lemmatize(text)
        text = self.remove_stopwords(text)
        return text
