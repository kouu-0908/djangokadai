from django.urls import path
from . import views
 
app_name = 'touroku'
 
urlpatterns = [
    path('kouryaku-touroku/', 
        views.TourokuView.as_view(),
        name ='kouryaku_touroku'),
]