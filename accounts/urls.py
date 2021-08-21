from django.urls import path, include
import django.contrib.auth.urls as auth_urls

from accounts.views import UserCreationView

urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='sign_up'),
    path('', include(auth_urls)),
]