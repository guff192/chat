from django.urls import path

from chat import views

urlpatterns = [
    path('', views.MessageListView.as_view(), name='chat'),
]