from django.shortcuts import render
from . import models
from . import forms
from django.views import View
  

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
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')

        # Usuário logado
        if self.request.user.is_authenticated:
            pass

        # Usário não logado (novo)
        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        return self.render
        

