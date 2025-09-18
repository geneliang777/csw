# yourapp/llm.py
import google.generativeai as genai
import os

import requests
import base64
import json
import re
from typing import Tuple, Optional

# Helper: 檢查是否像 base64 字串
_base64_re = re.compile(r'^[A-Za-z0-9+/=\s]+$')

def call_gemini(role_prompt: str, question: str, context: str = "") -> str:
    """
    呼叫 Gemini 模型並取得回答（可選擇傳入 context）
    """
    try:
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-pro')

        # 建 Prompt：明確要求「先用 context，再回答；沒有就說不知道」
        full_prompt = f"""{role_prompt}

你會依據「已知資料」回答，並避免臆測。

[已知資料]
{context if context else "（無）"}

[使用者問題]
{question}
"""

        response = model.generate_content(full_prompt)
        return response.text

    except Exception as e:
        print(f"呼叫 Gemini 發生錯誤: {e}")
        return "很抱歉，無法處理您的請求，請稍後再試。"



def _looks_like_base64(s: str) -> bool:
    if not isinstance(s, str):
        return False
    s2 = s.strip()
    return len(s2) > 100 and bool(_base64_re.match(s2))

def _extract_base64(obj) -> Optional[Tuple[str, Optional[str]]]:
    """
    嘗試從回傳 JSON（可能結構不固定）遞歸找出第一個 imageBytes 或 image 圖片字串與 mimeType
    回傳 (base64_str, mimeType) 或 None
    """
    if isinstance(obj, dict):
        # 常見位置
        if 'imageBytes' in obj and isinstance(obj['imageBytes'], str):
            return obj['imageBytes'], obj.get('mimeType')
        if 'image' in obj:
            image = obj['image']
            if isinstance(image, dict):
                if 'imageBytes' in image and isinstance(image['imageBytes'], str):
                    return image['imageBytes'], image.get('mimeType')
                # 有些版本可能直接 image: "<base64>"
                if isinstance(image, str) and _looks_like_base64(image):
                    return image, None
        # 搜尋子鍵
        for v in obj.values():
            found = _extract_base64(v)
            if found:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = _extract_base64(item)
            if found:
                return found
    elif isinstance(obj, str):
        if _looks_like_base64(obj):
            return obj, None
    return None



def call_gemini_image(prompt: str, model: str = "imagen-3.0-generate-002") -> Tuple[bytes, str]:
    """
    使用 REST 呼叫 Imagen (Gemini) 產生圖片。
    回傳 (image_bytes, mime_type)；失敗會 raise Exception。
    註：model 可改成 "imagen-3.0-fast-generate-001" 或其他你有權限的版本。
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set in environment")

    # 建議使用 Gemini 的 Generative Language endpoint (v1beta)：
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predict"
    headers = {
        "Content-Type": "application/json",
        # 用 API key 時常用 x-goog-api-key；有時也可用 ?key=... 或 Authorization Bearer token
        "x-goog-api-key": api_key,
    }

    payload = {
        "instances": [
            {
                "prompt": prompt
            }
        ],
        "parameters": {
            # sampleCount 或 numberOfImages 依 API 與 model 而異，這裡示範常見參數
            "sampleCount": 1,
            "numberOfImages": 1,
            "aspectRatio": "9:16"
        }
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        # 加一點除錯資訊
        raise RuntimeError(f"HTTP error: {e}, body: {resp.text}")

    data = resp.json()

    found = _extract_base64(data)
    if not found:
        # 如果沒有找到，直接把整個回應存成檔案方便除錯
        raise RuntimeError(f"No image found in response: {json.dumps(data)[:2000]}")

    b64_str, mime = found
    try:
        img_bytes = base64.b64decode(b64_str)
    except Exception as e:
        raise RuntimeError(f"Failed to decode base64 image: {e}")

    # 預設 mime type
    if not mime:
        mime = "image/png"
    return img_bytes, mime