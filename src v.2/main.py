from data_preprocessor import DataPreprocessor
from data_visualizer import DataVisualizer
from model_trainer import ModelTrainer

# Создайте экземпляры классов
preprocessor = DataPreprocessor()
visualizer = DataVisualizer()
trainer = ModelTrainer()

# Пример использования:
# processed_text = preprocessor.preprocess("Пример текста для предобработки.")
# visualizer.plot_wordcloud(processed_text)
# trainer.train_model(X_train, y_train, model) # Где X_train, y_train, model - ваши данные и модель

# Добавьте сюда логику загрузки данных, их предобработки, визуализации и обучения модели.
