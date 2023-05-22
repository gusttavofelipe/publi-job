from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views import View
from . import models
from . import forms
  

class BaseRegister(View):
    template_name = 'user/register.html' 

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.profile = None

        if self.request.user.is_authenticated:  
            self.profile = models.Profile.objects.filter(username=self.request.user)

            self.context = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None,
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
        
        password = self.userform.cleaned_data.get('password')

        # Usuário logado
        if not self.request.user.is_authenticated:

            userr = self.userform.save(commit=False)
            userr.set_password(password)
            userr.save()

            profile = self.profileform.save(commit=False)
            profile.userr = userr
            profile.save()

        if password:
            check = authenticate(
                self.request,
                user=userr,
                password=password
                )
            if check:
                login(self.request, user=userr)

        messages.success(
            self.request,
            'Registered successfully'
        )
        
        return redirect('vacancies:home') 
        
    
class UserLogin(BaseRegister):
    template_name = 'user/login.html'

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')

        if not email or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('user:user_login')

        usuario = authenticate(
            self.request, email=email, password=password)

        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('user:user_login')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Você fez login no sistema e pode concluir sua compra.'
        )
        return redirect('produto:carrinho')


class UserLogout(BaseRegister):
    template_name = 'user/login.html'

    def post(self, *args, **kwargs):
        logout(self.request)
        return redirect('vacancies:home')
