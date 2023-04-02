
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.user.urls')),

    path('admin/', admin.site.urls),
]
