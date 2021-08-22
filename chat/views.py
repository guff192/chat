from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from chat.forms import NewMessageForm
from chat.models import Message


class MessageCreationView(CreateView):
    model = Message
    template_name = 'chat/chat.html'
    form_class = NewMessageForm
    success_url = reverse_lazy('chat')

    def get_context_data(self, **kwargs):
        context = super(MessageCreationView, self).get_context_data(**kwargs)
        context['message_list'] = Message.objects.all()
        return context

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sent_by = self.request.user
        message.save()
        messages.success(self.request, 'Сообщение отправлено')
        return super(MessageCreationView, self).form_valid(form)

