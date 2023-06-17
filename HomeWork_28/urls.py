from django.contrib import admin
from django.urls import path, include

from ads.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.MainView.as_view()),
    path("ads/", include("ads.urls.urls_ads")),
    path("cat/", include("ads.urls.urls_category")),
    path("user/", include("users.urls")),
]
