from sklearn.metrics import accuracy_score

class ModelTrainer:
    def train_model(self, X_train, y_train, model):
        model.fit(X_train, y_train)
        return model
    
    def evaluate_model(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy
