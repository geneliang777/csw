from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("menu")  # 登入成功 → 跳回首頁
            else:
                return render(request, "accounts/login.html", {
                    "form": form,
                    "error": "帳號或密碼錯誤"
                })
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")
