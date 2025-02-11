from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .import views
from myapp.views import RegisterView, ChangePasswordView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # User Registration
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('change-password/', ChangePasswordView.as_view(), name='change_password') 
]
