import os
import math
import numpy as np
import google.generativeai as genai
from .models import ProjectDocument 

def _cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)

def embed_text_gemini(text: str) -> np.ndarray:
    """
    取得文字的 embedding（使用 Google text-embedding-004）
    """
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    res = genai.embed_content(
        model="text-embedding-004",
        content=text,
    )
    vec = np.array(res["embedding"], dtype=float)
    return vec

def search_similar_docs(project_id: int, question: str, top_k: int = 3, min_score: float = 0.2):
    """
    回傳最相近的文件片段清單：
    [
      {"id": 123, "text": "...", "score": 0.87},
      ...
    ]
    """
    q_vec = embed_text_gemini(question)

    # 取出該專案下的所有向量與文本
    qs = ProjectDocument.objects.filter(project_id=project_id).values("id", "content", "embedding")
    #qs = Document.objects.filter(project_id=project_id).values("id", "text", "embedding")
    # ↑ 如果你的欄位不是 text / embedding，請改成你的欄位名

    hits = []
    for row in qs:
        emb = row["embedding"]
        if not emb:
            continue
        # embedding 可能是 list[float] 或字串(JSON)；確保變成 np.ndarray
        vec = np.array(emb, dtype=float)
        if vec.ndim != 1:
            continue

        if isinstance(emb, str):
            try:
                emb = json.loads(emb)
            except Exception:
                continue



        score = _cosine_similarity(q_vec, vec)
        if score >= min_score:
         
            hits.append({"id": row["id"], "text": row["content"], "score": score})
        
            

    # 依相似度排序、取前 top_k
    hits.sort(key=lambda x: x["score"], reverse=True)
    return hits[:top_k]