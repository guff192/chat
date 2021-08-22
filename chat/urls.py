from django.urls import path

from chat import views

urlpatterns = [
    path('', views.MessageCreationView.as_view(), name='chat'),
]