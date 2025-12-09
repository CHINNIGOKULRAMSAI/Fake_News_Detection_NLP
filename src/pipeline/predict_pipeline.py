import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
from src.components.data_transformation import DataTransformation

class PredictPipeline:
    def __init__(self):
        # Cache model and vectorizer for performance
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "vectorizer.pkl")
            self.model = load_object(file_path=model_path)
            self.preprocessor = load_object(file_path=preprocessor_path)
            self.dt = DataTransformation()
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            # Validate input list: always work with a list and always return an array
            if not isinstance(features, (list, tuple)):
                features = [features]

            # Clean raw text using DataTransformation._clean_text before vectorizing
            cleaned_features = [self.dt._clean_text(str(t) if t is not None else "") for t in features]
            data_scaled = self.preprocessor.transform(cleaned_features)
            preds = self.model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, text: str):
        self.text = text

    def get_data_as_list(self):
        try:
            return [self.text]
        except Exception as e:
            raise CustomException(e, sys)
