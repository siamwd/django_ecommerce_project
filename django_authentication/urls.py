from django.urls import path
from .views import HomeView, login_view, logout_view, register_view

app_name ="django_authentication"
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('login/', login_view, name="login"),
    path('logout/',logout_view, name="logout"),
    path('register/',register_view,name="register")
]