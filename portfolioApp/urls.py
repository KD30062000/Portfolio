from django.urls import path,include
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('download',views.download,name='download'),
    path('subscribe',views.subscribe,name='subscribe')
]