# Anime Search & Recommendation (Image Search & Recommender)

**Status:** 🚧 In progress (early prototype; endpoints and indices under active development)

## Overview
This is an experimental ML service where users upload a **screenshot** to find related anime scenes, with content-based recommendations.  
It demonstrates end-to-end retrieval: data preparation → embeddings → vector search → API → UI.  

> ⚠️ Note: This project uses only publicly available images or low-resolution screenshots for demonstration purposes to avoid copyright issues.  

## Core Capabilities (Planned)
- **Image search:** CLIP-style embeddings + FAISS for similarity retrieval  
- **Content-based recommendations:** Initially using item similarity; light collaborative filtering may be added later  
- **Latency optimizations:** Warm-up, batching, caching  

## Tech Stack
- Frontend: Next.js  
- Backend: FastAPI (Python)  
- Machine Learning: PyTorch / Hugging Face  
- Vector Search: FAISS (POC) → Milvus/Weaviate (for scalable deployment)  
- DevOps: Docker & GitHub Actions  

## Roadmap
1. Subtitle index + text search  
2. Image embeddings + FAISS search  
3. Content-based recommendations  
4. Profiling & small-scale deployment  

## Project Scope
This project is intended for **research and educational purposes**, demonstrating anime image retrieval and recommendation.  
All media used are either publicly available or sourced with proper attribution. No copyrighted full episodes or audio are used.
