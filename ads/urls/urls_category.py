from django.urls import path

from ads.views import views_categories

urlpatterns = [
    path('', views_categories.CategoryListView.as_view()),
    path('<int:pk>/', views_categories.CategoryDetailView.as_view()),
    path('create/', views_categories.CategoryCreateView.as_view()),
    path('<int:pk>/update/', views_categories.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', views_categories.CategoryDeleteView.as_view()),
]