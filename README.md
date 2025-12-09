# 📰 Fake News Detection – NLP + FastAPI

An end-to-end Fake News Detection system built with NLP and Machine Learning.
The app exposes a FastAPI service and a modern web UI to classify news text as
**REAL** or **FAKE** using a model trained on the **WELFake** dataset.

## 🚀 Features

- Data ingestion from WELFake CSV/ZIP
- Text cleaning: lowercasing, HTML removal, stopword removal, lemmatization
- TF–IDF vectorization (word or character n-grams)
- Model training with:
  - Logistic Regression
  - Linear SVM (LinearSVC)
  - Passive Aggressive Classifier
- Hyperparameter tuning via RandomizedSearchCV (balanced accuracy)
- Best model + vectorizer saved as artifacts (`model.pkl`, `vectorizer.pkl`)
- FastAPI backend with `/predict` endpoint
- Modern frontend (HTML + TailwindCSS) calling the API
- Health endpoint for monitoring

## 🗂 Project Structure

```bash
Fake_News_Detection_NLP/
│
├─ data/                     # raw dataset (WELFake_Dataset.csv.zip)
├─ artifacts/                # saved model, vectorizer, train/test splits
├─ logs/                     # training and runtime logs
├─ notebook/                 # experiments and EDA
├─ src/
│   ├─ components/
│   │   ├─ data_ingestion.py
│   │   ├─ data_transformation.py
│   │   └─ model_training.py
│   ├─ pipeline/
│   │   ├─ train_pipeline.py
│   │   └─ predict_pipeline.py
│   ├─ exception.py
│   ├─ logger.py
│   └─ utils.py
├─ templates/
│   └─ index.html            # web UI
├─ static/
│   └─ style.css             # custom styles (optional)
├─ main.py                   # FastAPI app
├─ requirements.txt
└─ setup.py
