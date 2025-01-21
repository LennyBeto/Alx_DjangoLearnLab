from django.urls import path
from .views import user_registration, CustomAuthToken, user_profile

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('profile/', user_profile, name='user-profile'),
]
