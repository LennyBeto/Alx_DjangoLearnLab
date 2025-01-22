from django.urls import path
from .views import user_registration, CustomAuthToken, user_profile, FollowView, UnfollowView

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('profile/', user_profile, name='user-profile'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
]

