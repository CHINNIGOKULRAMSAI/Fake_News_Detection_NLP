# 📰 Fake News Detection — NLP · FastAPI · Docker · Azure

### Real-time Fake News Classification System powered by Machine Learning, built for production deployment with FastAPI, Docker, and Azure App Service.


👉 Live App URL:
https://fake-news-app-gokul.azurewebsites.net


---

## 🚀 Tech Stack

**ML / NLP**: scikit-learn · TF-IDF
**Backend**: FastAPI · Uvicorn
**Deployment**: Docker · Azure Container Registry · Azure App Service
**UI**: HTML · TailwindCSS

---

## ✨ Features

* 🔎 **Real-time Fake/Real news prediction**
* 🧹 **End-to-end NLP pipeline** (cleaning, tokenizing, vectorizing)
* ⚙️ **Modular ML workflow** (training + prediction pipelines)
* 🌐 **FastAPI REST API** with health & prediction endpoints
* 🐳 **Dockerized application** for easy deployment
* ☁️ **Hosted on Azure App Service** using ACR images
* 🎨 **Modern web UI** with “Try REAL” and “Try FAKE” examples

---

## 📁 Project Structure

```
project/
│── src/
│   ├── components/          # ingestion, transformation, training modules
│   ├── pipeline/            # train & predict pipelines
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│
│── artifacts/               # model, vectorizer, processed data
│── main.py                  # FastAPI application
│── index.html               # Frontend UI
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 🧪 API Endpoints

### Health Check

`GET /health`

### Predict Fake/Real

`POST /predict`

```json
{
  "text": "Your news article here..."
}
```

---

## 🖥️ Running Locally

### Install

```bash
pip install -r requirements.txt
```

### Start App

```bash
uvicorn main:app --reload
```

UI available at:

```
http://localhost:8000
```

---

## 🐳 Docker

### Build

```bash
docker build -t fake-news-api:v1 .
```

### Run

```bash
docker run -p 8000:8000 fake-news-api:v1
```

---

## ☁️ Azure Deployment (Container-Based)

### Push Image to ACR

```bash
docker tag fake-news-api:v1 <ACR_NAME>.azurecr.io/fake-news-api:v1
docker push <ACR_NAME>.azurecr.io/fake-news-api:v1
```

### Configure Web App

```bash
az webapp config container set \
  --name <WEBAPP_NAME> \
  --resource-group <RG_NAME> \
  --container-image-name <ACR_NAME>.azurecr.io/fake-news-api:v1 \
  --container-registry-url https://<ACR_NAME>.azurecr.io \
  --container-registry-user <USER> \
  --container-registry-password "<PASSWORD>"
```

### Set App Port

```bash
az webapp config appsettings set \
  --resource-group <RG_NAME> \
  --name <WEBAPP_NAME> \
  --settings WEBSITES_PORT=8000
```

---

## 🎨 UI Preview

The frontend includes:

* Clean TailwindCSS interface
* Input box for article text
* Real-time prediction display
* Auto-filled example articles (Real / Fake)

---

## 📌 Highlights

* Fully production-ready design
* Easy CI/CD integration
* Cloud-native architecture
* Perfect for portfolio + resume + interviews
* Real-world MLOps project structure

---

## 📜 License

MIT License.

---
