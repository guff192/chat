from django.views.generic import ListView

from chat.models import Message


class MessageListView(ListView):
    model = Message
    template_name = 'chat/chat.html'
