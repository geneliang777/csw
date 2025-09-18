from django.shortcuts import render
from core.models import Menu
from django.contrib.auth.decorators import login_required

# def menu(request):
#     return render(request, "menu.html")

@login_required
def menu(request):
    # 只撈出「父選單」(parent 為空的)
    menus = Menu.objects.filter(parent__isnull=True, is_active=True).order_by("order")
    print(menus)
    print('menu')
    return render(request, "menu.html", {"menus": menus})



@login_required
def home(request):
    return render(request, "home.html", {"params": {}})    

@login_required
def short(request):
    return render(request, "short.html", {"params": {}})    

@login_required
def short_modular(request):
    return render(request, "short_modular.html", {"params": {}})    

@login_required
def photo(request):
    return render(request, "photo.html", {"params": {}})    

@login_required
def story(request):
    return render(request, "story.html", {"params": {}})    

    