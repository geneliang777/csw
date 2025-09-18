
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Menu
from .forms import MenuForm

# def menu(request):
#     # 只撈出「父選單」(parent 為空的)
#     menus = Menu.objects.filter(parent__isnull=True, is_active=True).order_by("order")
#     print(menus)
#     print('menu')
#     return render(request, "menu.html", {"menus": menus})
# def menu(request):
#     menus = Menu.objects.filter(parent__isnull=True, is_active=True).order_by("order")
#     return render(request, "menu.html", {"menus": menus})
# def menu(request):
#     # 只抓父選單（啟用）
#     menus = Menu.objects.filter(parent__isnull=True, is_active=True).order_by('order')

#     # 將子選單也過濾掉停用的
#     for menu in menus:
#         menu.active_children = menu.children.filter(is_active=True).order_by('order')

#     return render(request, 'menu.html', {'menus': menus})
# def menu(request):
#     menus = Menu.objects.filter(parent__isnull=True, is_active=True).prefetch_related('children')
#     return render(request, 'menu.html', {'menus': menus})
# def menu(request):
#     # 只抓父選單，並且啟用
#     menus = Menu.objects.filter(parent__isnull=True, is_active=True)
#     return render(request, 'menu.html', {'menus': menus})


def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@login_required
@admin_required
# def menu_list(request):
#     menus = Menu.objects.all().select_related('parent').order_by('parent__id', 'order')
#     return render(request, 'core/menu_list.html', {'menus': menus})

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, "core/menu_list.html", {"menus": menus})

@login_required
@admin_required
def menu_add(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'core/menu_form.html', {'form': form, 'action': '新增'})

@login_required
@admin_required
def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'core/menu_form.html', {'form': form, 'action': '編輯'})

@login_required
@admin_required
def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'core/menu_confirm_delete.html', {'menu': menu})


