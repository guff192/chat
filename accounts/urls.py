from django.urls import path, include
import django.contrib.auth.urls as auth_urls

from accounts.views import UserCreationView, get_user_profile, change_profile

urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='sign_up'),
    path('profile/', get_user_profile, name='profile'),
    path('change_profile/', change_profile, name='change-profile'),
    path('', include(auth_urls)),
]