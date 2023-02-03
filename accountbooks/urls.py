from django.urls import path
from accountbooks import views

urlpatterns = [
    path('', views.AccountbookView.as_view(), name="accountbook_view"),
    path('<int:accountbook_id>/', views.AccountbookDetailView.as_view(), name="accountbook_detail_view"),
]
