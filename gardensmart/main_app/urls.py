from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('veggies/', views.veggies_index, name='index'),    
    path('veggies/<int:veg_id>', views.veg_detail, name='detail'),
]