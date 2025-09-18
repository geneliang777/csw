"""
URL configuration for csw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.menu, name='menu')
Class-based views
    1. Add an import:  from other_app.views import menu
    2. Add a URL to urlpatterns:  path('', menu.as_view(), name='menu')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from demo.views import demo_view
from django.contrib import admin
from django.urls import path
from csw.views import menu,home,short,short_modular,photo,story
from accounts.views import user_login, user_logout





urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo_view), # Include demo app URLs
    path("", menu, name="menu"),
    path("home", home, name="home"),
    path("short", short, name="short"),
    path("short_modular", short_modular, name="short_modular"),
    path("photo", photo, name="photo"),
    path("story", story, name="story"),
    path("home", home, name="home"),
    path("home", home, name="home"),
    path("login/", user_login, name="login"),
    path("accounts/login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),  
    path("accounts/logout/", user_logout, name="logout"),  
    path('', include('core.urls')),  # 首頁
    path('accounts/', include('django.contrib.auth.urls')),  # 登入/登出  
    path('project/', include('projects.urls')),   # ← 新增這行，會得到 /project/new
   
]
