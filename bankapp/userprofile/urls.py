from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_home, name="home"),
    path('download/', views.download_bank_statement, name='download_bank_statement'),
]