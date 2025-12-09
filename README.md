📰 Fake News Detection using NLP | FastAPI | Docker | Azure App Service

This project is an end-to-end MLOps-ready Fake News Classification System built using:

NLP preprocessing

TF-IDF vectorization

Logistic Regression classifier

FastAPI backend

Interactive frontend

Docker containerization

Azure Container Registry

Azure App Service deployment

The system predicts whether a given news article is REAL or FAKE based on learned linguistic patterns.


👉 Live App URL:
https://fake-news-app-gokul.azurewebsites.net


📌 Features
🔹 Machine Learning

Built using the WELFake dataset (72K samples)

Full NLP preprocessing pipeline:

Lowercasing

Stopword removal

Special character cleaning

HTML tag removal

URL removal

Lemmatization

TF-IDF vectorizer + Logistic Regression model

Accuracy: 93%+ after tuning

🔹 FastAPI Web Service

/predict endpoint for real-time inference

/health endpoint for app monitoring

Clean modular architecture (src/components, src/pipeline, src/utils, etc.)

🔹 Frontend

A modern TailwindCSS-powered UI:

Live text input

Predictions with colored labels

Confidence score display

Example "Try REAL" and "Try FAKE" buttons

🔹 Dockerization

Production-ready Dockerfile

.dockerignore optimized for smaller image size

🔹 Azure Deployment

Container pushed to Azure Container Registry (ACR)

Deployed on Azure App Service (Linux)

Exposed via public URL

📁 Folder Structure
Fake_News_Detection_NLP/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_training.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│
├── artifacts/
│   ├── model.pkl
│   ├── vectorizer.pkl
│   ├── cleaned_data.csv
│
├── main.py                 → FastAPI app
├── index.html              → UI
├── Dockerfile
├── requirements.txt
├── README.md
└── .dockerignore

🧠 Model Pipeline Overview
1️⃣ Data Ingestion

Loads WELFake dataset

Drops missing values

Combines headline + text (if needed)

Saves clean CSV to artifacts/

2️⃣ Data Transformation

Cleans all text using:

Regex filters

Stopwords

Lemmatizer
Outputs:

vectorizer.pkl (TF-IDF model)

3️⃣ Model Training

Trains Logistic Regression

Evaluates accuracy

Saves model.pkl

4️⃣ Prediction Pipeline

Takes text → cleans → vectorizes → predicts → returns label + probability

▶️ Running Locally (without Docker)
Install dependencies
pip install -r requirements.txt

Start FastAPI app
uvicorn main:app --reload


Open browser:
👉 http://127.0.0.1:8000

🐳 Docker Setup
1️⃣ Build Docker image
docker build -t fake-news-api:v1 .

2️⃣ Run container
docker run -p 8000:8000 fake-news-api:v1


Open browser:
👉 http://localhost:8000

☁️ Azure Deployment Guide (ACR + App Service)
1️⃣ Login to Azure
az login

2️⃣ Create Resource Group
az group create --name fake-news-rg --location centralindia

3️⃣ Create Azure Container Registry (ACR)
az acr create --resource-group fake-news-rg --name fakenewsacr98765 --sku Basic


Enable admin:

az acr update --name fakenewsacr98765 --admin-enabled true

4️⃣ Tag and Push Docker Image
docker tag fake-news-api:v1 fakenewsacr98765.azurecr.io/fake-news-api:v1
docker push fakenewsacr98765.azurecr.io/fake-news-api:v1

5️⃣ Create App Service Plan
az appservice plan create --name fake-news-plan --resource-group fake-news-rg --sku B1 --is-linux

6️⃣ Create Web App
az webapp create --resource-group fake-news-rg --plan fake-news-plan --name fake-news-app-gokul --deployment-container-image-name fakenewsacr98765.azurecr.io/fake-news-api:v1

7️⃣ Configure ACR Credentials
az webapp config container set --name fake-news-app-gokul --resource-group fake-news-rg --container-image-name fakenewsacr98765.azurecr.io/fake-news-api:v1 --container-registry-url https://fakenewsacr98765.azurecr.io --container-registry-user fakenewsacr98765 --container-registry-password "YOUR_PASSWORD"

8️⃣ Set port
az webapp config appsettings set --resource-group fake-news-rg --name fake-news-app-gokul --settings WEBSITES_PORT=8000

9️⃣ Restart webapp
az webapp restart --resource-group fake-news-rg --name fake-news-app-gokul



🧪 API Endpoints
Health Check
GET /health

Prediction
POST /predict
{
   "text": "your news article here"
}


Response:

{
  "label": "FAKE NEWS",
  "prediction": 1,
  "confidence": 0.97
}

🎨 UI Preview

TailwindCSS modern UI

Real/Fake example buttons

Highlighted prediction box

Confidence display

🛠 Tech Stack
Layer	Technology
ML	Python, scikit-learn, nltk
NLP	TF-IDF, lemmatization
API	FastAPI, Uvicorn
Frontend	HTML + TailwindCSS
Deployment	Docker, ACR, Azure App Service
🚀 Future Enhancements

Use Transformers (BERT / DistilBERT)

Add headline + body combination

Add explainability (LIME / SHAP)

Create CI/CD pipeline using GitHub Actions

Add database for storing predictions

🙌 Acknowledgements

WELFake Dataset

FastAPI team

Azure cloud platform