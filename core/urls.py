from django.urls import path

from . import views 

urlpatterns = [
   
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/add/', views.menu_add, name='menu_add'),
    path('menus/<int:pk>/edit/', views.menu_edit, name='menu_edit'),
    path('menus/<int:pk>/delete/', views.menu_delete, name='menu_delete'),
    path("menus/", views.menu_list, name="menu_list"),
]