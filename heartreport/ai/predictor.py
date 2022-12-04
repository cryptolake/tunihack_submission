from tensorflow import keras
import numpy as np

class Predictor:
    """Class to talk to the model"""
    def __init__(self, path):
        """Initialize model"""
        self.model = keras.models.load_model(path)
    
    def __preprocess_data(self, data):
       array  = np.asarray(list(dict(data).values())).astype(float).reshape((1, 10))
       print(array)
       return array

    
    def predict(self, data):
        pre_data = self.__preprocess_data(data)
        result = self.model.predict(pre_data)
        result = float(result[0, 0])
        return result 