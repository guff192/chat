from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserSignUpForm


class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'

    def form_valid(self, form):
        messages.success(self.request, 'Регистрация успешно завершена')
        return super(UserCreationView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Проверьте правильность введённых данных!')
        return super(UserCreationView, self).form_invalid(form)



