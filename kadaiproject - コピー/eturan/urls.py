from django.urls import path
from . import views

app_name ='eturan'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    
    path('kouryaku-detail/',
         views.DetailView.as_view(),
         name='kouryaku_detail'),
    
    path('kouryaku-mail/',
         views.MailView.as_view(),
         name='kouryaku_mail'),
]
