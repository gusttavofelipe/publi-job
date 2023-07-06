from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic import ListView
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import UpdateView
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView


class BaseRegister(View):
    template_name = 'user/register.html' 

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.profile = None

        if self.request.user.is_authenticated:  
            self.profile = Profile.objects.filter(
                username_profile=self.request.user
            ).last()
            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None,
                    instance=self.profile,
                )
            }

        else:
            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None
                )
            }

        self.userform = self.context['userform']
        self.profileform = self.context['profileform']
    
        self.render = render(
            self.request, self.template_name, self.context
        )
    
    def get(self, *args, **kwargs):
        return self.render


class UserRegister(BaseRegister):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.profileform.is_valid():
            return self.render
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')

        if not self.request.user.is_authenticated:

            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.username_profile = user
            profile.save()

        if password:
            check = authenticate(
                self.request,
                username=username,
                password=password
                )
            if check:
                login(self.request, user=user)


        messages.success(
            self.request,
            'Registered successfully'
        )
        
        return redirect('vacancies:home') 
        
    
class UserLogin(BaseRegister):
    template_name = 'user/login.html'

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            return redirect('user:user_login')

        user = authenticate(
            self.request, username=username, password=password)

        if not user:
            return redirect('user:user_login')

        login(self.request, user=user)
        return redirect('vacancies:home')


class UserLogout(BaseRegister):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('vacancies:home')


class UserProfile(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'user/profile.html'


class EditUserInformation(UpdateView):
    template_name = 'user/edit.html'
    model = User
    fields = ['first_name', 'last_name', 'email', 'username']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('vacancies:home')

    def get_object(self):
        return self.request.user
    

class ChangePassword(PasswordChangeView):
    template_name='user/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('vacancies:home')

