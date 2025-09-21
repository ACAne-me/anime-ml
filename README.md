## Anime Search & Recommendation (ASR, Image Search, Recommender)
**Status:** 🚧 **In progress** (early prototype; endpoints and indices under active development)

**Overview.**  
An experimental ML service where users upload a short **audio clip** or **screenshot** to find related anime scenes, with content-based recommendations. Demonstrates end-to-end retrieval: data prep → embeddings → vector search → API → UI.

**Core capabilities (planned).**  
ASR search (audio → transcript → subtitle match), image search (CLIP-style embeddings + FAISS), content-based recommendations first (light CF later), and latency levers (warm-up, batching, caching).

**Tech stack.** Next.js; FastAPI (Python); PyTorch / Hugging Face; FAISS (POC) → Milvus/Weaviate (scalable). Docker & GitHub Actions.

**Roadmap.**  
Phase 1: subtitle index + text search → Phase 2: ASR integration → Phase 3: image embeddings + FAISS → Phase 4: recommendations → Phase 5: profiling & small deploy.
