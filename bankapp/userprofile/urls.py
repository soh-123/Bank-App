from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_home, name="home"),
    path('download/', views.download_bank_statement, name='download_bank_statement'),
    path('send_email/', views.send_email, name='send_email'),
    path('filter_transactions/', views.filter_transactions, name='filter_transactions'),

]