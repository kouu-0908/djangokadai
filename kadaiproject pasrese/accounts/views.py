from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

#サインアップするページのview
class SignUpView(CreateView):
    form_class =CustomUserCreationForm
    template_name ="signup.html"
    success_url =reverse_lazy('accounts:signup_success')
    
    def form_valid(self, form):
        user =form.save()
        self.object =user
        return super().form_valid(form)
    
#サインアップ完了した時に表示させるページのview
class SignUpSuccessView(TemplateView):
    template_name ="signup_success.html"
