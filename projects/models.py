from django.db import models
from django.conf import settings

class LLMProject(models.Model):
    project_code = models.CharField("專案代碼",max_length=20, unique=True, null=True, blank=True)
    name = models.CharField("專案名稱", max_length=100)
    description = models.TextField("說明",blank=True, null=True)
    llm_model = models.CharField(
        "LLM 模型",
        max_length=50,
        choices=[
            ("gemini", "Gemini"),
            ("gpt-5", "GPT‑5"),
            ("gpt-4o", "GPT‑4o"),
            ("local", "Llama"),
        ],
    )
    embedding_engine = models.CharField(
        "向量化引擎",
        max_length=50,
        choices=[
            ("text-embedding-3-large", "OpenAI text-embedding-3-large"),
            ("bge-large", "BGE Large"),
            ("cohere-v3", "Cohere embed-english-v3"),
        ],
        null=True, 
        blank=True,
    )
    role_prompt = models.TextField("角色指令定義", blank=True)
    response_template = models.TextField("回應模板配置", blank=True)
    example_prompts = models.TextField("範例提示詞（每行一個）", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_code} - {self.name}"
    

class ProjectDocument(models.Model):
    project = models.ForeignKey('LLMProject', on_delete=models.CASCADE, related_name='documents')
    filename = models.CharField(max_length=512)
    uploaded_file = models.FileField(upload_to='project_imports/%Y/%m/%d', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    embedding = models.JSONField(blank=True, null=True) # 存向量 (list) 或 metadata
    imported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    imported_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.project} - {self.filename}"