from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_squared_log_error
import numpy as np
import pickle
from scripts.logger import Logger

class ModelTrainer:
    def __init__(self, logger=None):
        self.logger = logger if logger else Logger('rossmann_analysis.log')
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train_model(self, X_train, y_train):
        self.logger.log('Training the Random Forest model.')
        self.model.fit(X_train, y_train)
        self.logger.log('Model training complete.')
        
    def predict(self, X):
        self.logger.log('Making predictions.')
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        # Predict the test data
        y_pred = self.predict(X_test)

        # Calculate the evaluation metrics
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        msle = mean_squared_log_error(y_test, y_pred)

        # Logging the results
        self.logger.log(f"Mean Squared Error (MSE): {mse}")
        self.logger.log(f"Mean Absolute Error (MAE): {mae}")
        self.logger.log(f"Root Mean Squared Error (RMSE): {rmse}")
        self.logger.log(f"R-squared (R2): {r2}")
        self.logger.log(f"Mean Squared Logarithmic Error (MSLE): {msle}")

        # Print the results
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"Mean Absolute Error (MAE): {mae}")
        print(f"Root Mean Squared Error (RMSE): {rmse}")
        print(f"R-squared (R2): {r2}")
        print(f"Mean Squared Logarithmic Error (MSLE): {msle}")

        return mse, mae, rmse, r2, msle

    def save_model(self, model_file_path):
        self.logger.log(f'Saving the model to {model_file_path}')
        with open(model_file_path, 'wb') as f:
            pickle.dump(self.model, f)
        self.logger.log('Model saved successfully.')

    def load_model(self, model_file_path):
        self.logger.log(f'Loading the model from {model_file_path}')
        with open(model_file_path, 'rb') as f:
            self.model = pickle.load(f)
        self.logger.log('Model loaded successfully.')
