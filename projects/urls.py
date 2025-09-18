from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.project_new, name="project_new"),
    path("<int:pk>", views.project_detail, name="project_detail"),
    # 新增這兩個
    path("edit/", views.project_edit_search, name="project_edit_search"),
    path("edit/<int:pk>", views.project_edit, name="project_edit"),
    # 新增這兩條
    path("edit/<int:pk>/test", views.project_test, name="project_test"),         # popup HTML
    path("edit/<int:pk>/test_api", views.project_test_api, name="project_test_api"), # POST -> JSON
    path("edit/<int:pk>/generate_image", views.project_generate_image_api, name="project_generate_image_api"),
    path('edit/<int:pk>/import/', views.project_import, name='project_import'),
    path('edit/<int:pk>/import/<int:doc_pk>/', views.project_import_detail, name='project_import_detail'),
    path('edit/<int:pk>/import/<int:doc_pk>/delete/', views.project_import_delete, name='project_import_delete'),
    path("publish/", views.project_publish, name="project_publish"),
    path('edit/<int:pk>/export_sql/', views.project_export_sql, name='project_export_sql'),
    path('edit/<int:pk>/export_project_sql/', views.project_export_project_sql, name='project_export_project_sql'),
    path('edit/<int:pk>/export_example_html/', views.project_export_example_html, name='project_export_example_html'),
    path('edit/<int:pk>/crawl/', views.project_crawl, name='project_crawl'),

]