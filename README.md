# 🚀 **FAKE NEWS DETECTION — NLP + FASTAPI + DOCKER + AZURE**

### *A Production-Ready Fake News Classifier deployed with Azure App Service*

<p align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cloud-Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
  <img src="https://img.shields.io/badge/Language-Python_3.10-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Model-ML_NLP-success?style=for-the-badge"/>
</p>

---

## 📌 **Live Demo**

### 🔹 **Frontend Web App:**

👉 [https://fake-news-app-gokul.azurewebsites.net](https://fake-news-app-gokul.azurewebsites.net)

### 🔹 **API Documentation (Swagger UI):**

👉 [https://fake-news-app-gokul.azurewebsites.net/docs](https://fake-news-app-gokul.azurewebsites.net/docs)

---

# ✨ Overview

This project is a **real-time Fake News Detection System** built using:

* **NLP preprocessing**
* **TF-IDF vectorization**
* **Logistic Regression classifier**
* **FastAPI backend**
* **Docker containerization**
* **Azure Container Registry (ACR)**
* **Azure App Service deployment**

The app classifies news text as:

✅ **REAL NEWS**
❌ **FAKE NEWS**

It also provides a **confidence score** and comes with a modern, responsive, Tailwind CSS-powered UI.

---

# 🖼️ Screenshots

### 🔹 Home Page

<img src="your-screenshot-1-url" width="700">

### 🔹 Prediction Example

<img src="your-screenshot-2-url" width="700">

### 🔹 Swagger API Docs

<img src="your-screenshot-3-url" width="700">

> Replace the URLs above with GitHub image links after uploading screenshots.

---

# 🧠 Features

### 🌟 **Core Capabilities**

* Real-time fake news classification
* Confidence score generation
* Clean UI with Tailwind CSS
* REST API built using FastAPI
* Model + vectorizer loading via pickle
* Robust preprocessing (stopwords, lemmatization)

### 🌐 **Cloud & DevOps**

* Dockerized ML application
* Secure ACR container hosting
* Deployed using Azure App Service (Linux)
* Built-in health endpoint `/health`
* Swagger docs auto-generated at `/docs`

---

# 🏗️ System Architecture

```
               ┌────────────────────────┐
               │      User Browser      │
               │  (Tailwind Frontend)   │
               └────────────┬───────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │       FastAPI API      │
               │   /predict /health     │
               └────────────┬───────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │    ML Model (TF-IDF +  │
               │ Logistic Regression )   │
               └────────────┬───────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │   Docker Container     │
               └────────────┬───────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │ Azure Container Registry│
               └────────────┬───────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │ Azure App Service       │
               └─────────────────────────┘
```

---

# 🔧 Tech Stack

| Layer                | Technology                                  |
| -------------------- | ------------------------------------------- |
| **Frontend**         | HTML, Tailwind CSS, JavaScript              |
| **Backend API**      | FastAPI                                     |
| **ML Model**         | Scikit-learn (TF-IDF + Logistic Regression) |
| **Containerization** | Docker                                      |
| **Cloud Deployment** | Azure ACR + Azure App Service               |
| **Monitoring**       | Azure Log Stream                            |

---

# 🚀 Local Development

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/CHINNIGOKULRAMSAI/Fake_News_Detection_NLP.git
cd Fake_News_Detection_NLP
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI App

```bash
uvicorn main:app --reload --port 8000
```

Now open:
👉 `http://127.0.0.1:8000` (Frontend)
👉 `http://127.0.0.1:8000/docs` (Swagger)

---

# 🐳 Docker Setup

### Build Image

```bash
docker build -t fake-news-api:v1 .
```

### Run Container Locally

```bash
docker run -p 8000:8000 fake-news-api:v1
```

---

# ☁️ Azure Deployment (Production)

### Login to Azure

```bash
az login
```

### Push Image to ACR

```bash
docker tag fake-news-api:v1 fakenewsacr98765.azurecr.io/fake-news-api:v1
docker push fakenewsacr98765.azurecr.io/fake-news-api:v1
```

### Configure Web App to Pull Image

```bash
az webapp config container set \
  --name fake-news-app-gokul \
  --resource-group fake-news-rg \
  --container-image-name fakenewsacr98765.azurecr.io/fake-news-api:v1 \
  --container-registry-url https://fakenewsacr98765.azurecr.io \
  --container-registry-user fakenewsacr98765 \
  --container-registry-password "YOUR_PASSWORD"
```

### Set App Port

```bash
az webapp config appsettings set --name fake-news-app-gokul --resource-group fake-news-rg --settings WEBSITES_PORT=8000
```

---

# 📡 API Endpoints

| Method   | Endpoint   | Description            |
| -------- | ---------- | ---------------------- |
| **GET**  | `/`        | Returns frontend UI    |
| **GET**  | `/health`  | Health check           |
| **POST** | `/predict` | Predict fake/real news |
| **GET**  | `/docs`    | Swagger UI             |

---

# 📂 Project Structure

```
Fake_News_Detection_NLP/
│── data/
│── models/
│── static/
│── templates/
│── main.py
│── requirements.txt
│── Dockerfile
│── README.md
```

---

# ❤️ Credits

* Dataset: **WELFake**
* ML Framework: **Scikit-Learn**
* Deployment: **Microsoft Azure**

---

# ⭐ Support the Project

If you like this project, give it a ⭐ on GitHub!

👉 [https://github.com/CHINNIGOKULRAMSAI](https://github.com/CHINNIGOKULRAMSAI)

---
