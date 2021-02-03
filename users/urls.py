from django.urls import path
from rest_framework.authtoken import views

from users.views import UserRegister, UserRetrieveUpdateAPIView

urlpatterns = [
    path('auth/login', views.obtain_auth_token),
    # path('auth/current', CurrentUserView.as_view()),
    path('auth/current', UserRetrieveUpdateAPIView.as_view()),
    path('auth/register', UserRegister.as_view())
]
