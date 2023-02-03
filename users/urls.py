from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
