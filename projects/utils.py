import google.generativeai as genai
from django.conf import settings
import os

# def call_gemini(role_prompt, prompt):
#     """
#     呼叫 Gemini 模型並取得回答。
#     """
#     try:
#         # 設定 API 金鑰
#         genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        
#         # 選擇一個適合的 Gemini 模型
#         model = genai.GenerativeModel('gemini-1.5-pro')
        
#         # 結合角色指令和使用者問題，建立完整的提示詞
#         full_prompt = f"{role_prompt}\n\n使用者問題：{prompt}"
        
#         # 呼叫模型並取得回應
#         response = model.generate_content(full_prompt)
        
#         # 返回回答內容
#         return response.text

#     except Exception as e:
#         print(f"呼叫 Gemini 發生錯誤: {e}")
#         return "很抱歉，無法處理您的請求，請稍後再試。"