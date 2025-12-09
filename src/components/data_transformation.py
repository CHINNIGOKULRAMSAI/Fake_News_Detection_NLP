import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from scipy.sparse import hstack

import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('wordnet')


@dataclass
class DataTransformationConfig:
    vectorizer_path = os.path.join("artifacts", "vectorizer.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(
            max_features=20000,
            ngram_range=(1, 2),
            min_df=3,
            max_df=0.9,
            sublinear_tf=True
            )
    
    def _clean_text(self,text:str):
        if not isinstance(text, str):
            return ''
        text = text.lower()
        text = BeautifulSoup(text, "html.parser").get_text()
        text = re.sub(r'[^a-z0-9 ]+', ' ', text)
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(w) for w in tokens if w not in self.stopwords]

        return ' '.join(tokens)
    
    def initiate_data_transformation(self, train_path: str, test_path: str):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            train_df['text'] = train_df['text'].apply(self._clean_text)
            test_df['text'] = test_df['text'].apply(self._clean_text)

            X_train_text = train_df['text']
            X_train_target = train_df['label']

            X_test_text = test_df['text']
            X_test_target = test_df['label']

            X_train_vec = self.vectorizer.fit_transform(X_train_text)
            X_test_vec = self.vectorizer.transform(X_test_text)

            y_train = np.array(X_train_target).reshape(-1, 1)
            y_test = np.array(X_test_target).reshape(-1, 1)
            train_arr = hstack([X_train_vec, y_train])
            test_arr = hstack([X_test_vec, y_test])

            save_object(
                file_path=self.data_transformation_config.vectorizer_path,
                obj=self.vectorizer,
            )

            return (
                train_arr,
                test_arr,
            )


        except Exception as e:
            raise CustomException(e,sys)
