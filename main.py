from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
import numpy as np
import os

app = FastAPI(
    title="Fake News Detection API",
    description="Predict whether a news text is REAL or FAKE",
    version="1.0.0"
)

# --------------------------
# Serve index.html and static
# --------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve static files (optional style.css)
static_dir = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=FileResponse)
def serve_home():
    return FileResponse(os.path.join(BASE_DIR,"templates", "index.html"))

# --------------------------
# Prediction logic
# --------------------------

class NewsRequest(BaseModel):
    text: str

predict_pipeline = PredictPipeline()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_news(request: NewsRequest):
    text = (request.text or "").strip()
    if not text:
        return {
            "label": "Unknown",
            "prediction": None,
            "confidence": None,
            "error": "Empty text"
        }

    data = CustomData(text=text)
    texts = data.get_data_as_list()

    preds = predict_pipeline.predict(texts)
    pred = int(preds[0])

    # WELFake dataset → 0 = FAKE, 1 = REAL
    label = "REAL NEWS" if pred == 1 else "FAKE NEWS"

    confidence = None
    if hasattr(predict_pipeline.model, "predict_proba"):
        probs = predict_pipeline.model.predict_proba(
            predict_pipeline.preprocessor.transform(texts)
        )
        confidence = float(probs[0, pred])

    return {
        "label": label,
        "prediction": pred,
        "confidence": confidence
    }
