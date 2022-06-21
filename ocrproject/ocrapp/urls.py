from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.ocrhomepage, name="ocrhomepage"),
    path('register/', views.register, name="user.register"),
    path('login/', views.user_login, name="user.login"),
    path('dashboard/', views.user_dashboard, name="user.dashboard"),
    path('logout/', views.user_logout, name="user.logout")
]