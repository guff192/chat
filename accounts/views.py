from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserSignUpForm, ProfileForm, UserUpdateForm
from accounts.models import Profile


class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'

    def form_valid(self, form):
        messages.success(self.request, 'Регистрация успешно завершена')
        redirect = super(UserCreationView, self).form_valid(form)
        Profile.objects.create(user=self.object)
        return redirect

    def form_invalid(self, form):
        messages.error(self.request, 'Проверьте правильность введённых данных!')
        return super(UserCreationView, self).form_invalid(form)


def get_user_profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        context = {'profile': Profile.objects.filter(user=current_user).first()}
        return render(request, 'accounts/profile.html', context)
    else:
        return HttpResponseRedirect(reverse_lazy('login'))


def change_profile(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('profile'))

    if request.method != 'POST':
        user_form = UserUpdateForm(instance=current_user)
        profile_form = ProfileForm(instance=current_user.profile)
    else:
        user_form = UserUpdateForm(request.POST, instance=current_user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Данные сохранены')
            return redirect('profile')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/change_profile.html', context)
