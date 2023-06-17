from django.urls import path

from ads.views import views_ads

urlpatterns = [
    path('', views_ads.AdsListView.as_view()),
    path('create/', views_ads.AdsCreateView.as_view()),
    path('<int:pk>/', views_ads.AdsDetailView.as_view()),
    path('<int:pk>/update/', views_ads.AdsUpdateView.as_view()),
    path('<int:pk>/delete/', views_ads.AdsDeleteView.as_view()),
    path('<int:pk>/upload_image/', views_ads.AdsUploadImageView.as_view()),
]