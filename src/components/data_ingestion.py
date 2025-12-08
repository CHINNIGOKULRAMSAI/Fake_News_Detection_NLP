import numpy as np
import pandas as pd
import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import ModelTrainer
from src.components.model_training import ModelTrainerConfig


@dataclass
class DataIngestionConfig:
    train_path: str = os.path.join("artifacts", "train.csv")
    test_path: str = os.path.join("artifacts", "test.csv")
    raw_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion is Started")
            df = pd.read_csv("data/WELFake_Dataset.csv.zip", index_col=0)

            df = df[['title', 'text', 'label']].copy()
            df.dropna(subset=['title', 'text'], inplace=True)

            df.drop_duplicates(subset=['text', 'label'], inplace=True)

            df['text'] = (df['title'].fillna('') + ' ' + df["text"].fillna(''))

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_path, header=True, index=False)

            train_set, test_set = train_test_split(df[['text', 'label']], test_size=0.25, random_state=42, stratify=df['label'])

            train_set.to_csv(self.data_ingestion_config.train_path, header = True, index = False)
            test_set.to_csv(self.data_ingestion_config.test_path, header = True, index = False)

            return (
                self.data_ingestion_config.train_path,
                self.data_ingestion_config.test_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    DataIngestion = DataIngestion()
    train_path, test_path = DataIngestion.initiate_data_ingestion()

    DataTransformation = DataTransformation()
    train_arr, test_arr = DataTransformation.initiate_data_transformation(train_path, test_path)

    ModelTrainer = ModelTrainer()
    ModelTrainer.initiate_model_trainer(train_arr, test_arr)