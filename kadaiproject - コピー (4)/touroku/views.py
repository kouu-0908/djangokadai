from django.shortcuts import render
from django.views.generic.base import TemplateView
 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm,KategoriTuika
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class TourokuView(CreateView):
    form_class = PhotoPostForm
    template_name = "touroku.html"
    success_url = reverse_lazy('touroku:kouryaku_kanryou')
    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
 
class KanryouView(TemplateView):
    template_name = 'kanryou.html'
   
class KategoriView(CreateView):
    form_class = KategoriTuika
    template_name = "kategorituika.html"
    success_url = reverse_lazy('touroku:kouryaku_kanryou')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.save()
        return super().form_valid(form)
