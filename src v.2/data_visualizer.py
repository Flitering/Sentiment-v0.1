import matplotlib.pyplot as plt
from wordcloud import WordCloud

class DataVisualizer:
    def plot_wordcloud(self, text):
        wordcloud = WordCloud(background_color ='white').generate(text)
        plt.figure(figsize=(10, 10))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
