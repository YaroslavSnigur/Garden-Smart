from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('veggies/', views.veggies_index, name='index')
    path('accounts/signup/', views.signup, name='signup')
]