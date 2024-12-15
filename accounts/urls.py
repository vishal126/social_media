from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home', views.home, name="home"),
    path("login/", views.Login, name="login"),  # Ensure this matches "Login"
    path("register/", views.register, name="register"),
    path("logout/", views.Logout, name="logout"),  # Ensure this matches "Logout"
    # other paths...
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)