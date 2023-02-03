from django.urls import path
from accountbooks import views

urlpatterns = [
    path('', views.AccountbookView.as_view(), name="accountbook_view"),
]
