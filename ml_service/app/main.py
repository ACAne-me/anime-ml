from fastapi import FastAPI, UploadFile, File
from typing import List
import json, os

app = FastAPI(title="Anime ML Service")

# load sample subtitles
BASE = os.path.dirname(__file__)
with open(os.path.join(BASE, "../sample_data/sample_subs.json"), "r", encoding="utf8") as f:
    SUBS = json.load(f)

@app.post("/asr")
async def asr(file: UploadFile = File(...)):
    # TODO: 实接 ASR（whisper/torchaudio/huggingface）
    # 临时返回示例 transcript
    return {"transcript": "ここはサンプルの台詞です"}

@app.post("/search_by_text")
async def search_by_text(q: str):
    results = [s for s in SUBS if q in s["text"]]
    return {"results": results[:10]}

@app.post("/image-search")
async def image_search(file: UploadFile = File(...), top_k: int = 5):
    # TODO: 接 CLIP embedding + FAISS 检索
    return {"results": []}  # 占位
