from django import forms
from .models import LLMProject

class LLMProjectForm(forms.ModelForm):
    class Meta:
        model = LLMProject
        fields = ['project_code',"name",  "description", "llm_model", "embedding_engine", "role_prompt", "response_template", "example_prompts"]
        widgets = {
            "role_prompt": forms.Textarea(attrs={"rows":6, "placeholder":"你是公司的專屬 AI 助理，語氣專業、友善…"}),
            "response_template": forms.Textarea(attrs={"rows":6, "placeholder":"例如：\n{{greeting}}\n---\n{{answer}}"}),
            "example_prompts": forms.Textarea(attrs={"rows":4, "placeholder":"每行一個範例：\n請用50字介紹我們公司\n常見客戶問題有哪些？"}),
        }
        labels = {
            "name": "專案名稱",
            "llm_model": "LLM 模型",
            "embedding_engine": "向量化引擎",
        }
def clean_project_code(self):
    code = self.cleaned_data["project_code"]
    if LLMProject.objects.filter(project_code=code).exists():
        raise forms.ValidationError("這個專案代碼已存在，請換一個。")
    return code