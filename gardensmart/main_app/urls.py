from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('veggies/', views.veggies_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('inputs/', views.InputList.as_view(), name='inputs_index'),
    path('inputs/<int:pk>/', views.InputDetail.as_view(), name='inputs_detail'),
    path('inputs/create/', views.InputCreate.as_view(), name='inputs_create'),
    path('inputs/<int:pk>/update/', views.InputUpdate.as_view(), name='inputs_update'),
    path('inputs/<int:pk>/delete/', views.InputDelete.as_view(), name='inputs_delete'),
    path('veggies/<int:veg_id>', views.veg_detail, name='detail'),
    path('garden_store/', views.garden_store, name='garden_store'),
    path('veggies/create/', views.veggies_create, name='veg_create'),
    path('veggies/add/', views.veggies_add, name='veg_add'),
    path('veggies/<int:pk>/update/', views.VegUpdate.as_view(), name='veg_update'),
    path('veggies/<int:pk>/delete/', views.VegDelete.as_view(), name='veg_delete'),
    path('garden_store/<int:input_id>/assoc_input/', views.assoc_input, name='assoc_input'),
    path('garden_store/<int:input_id>/unassoc_input/', views.unassoc_input, name='unassoc_input'),
    path('veggies/<int:veg_id>/apply/<int:input_id>', views.input_apply, name='input_apply'),
]