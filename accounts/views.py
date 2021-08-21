from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserSignUpForm


class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'
