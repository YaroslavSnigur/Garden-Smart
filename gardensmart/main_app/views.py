from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Veg, Input
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#login and signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#User Signup function
def signup(request):
    error_message = ""

    #if signup is post, do this
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('about')
        
        else:
            error_message= form.errors

    #if GET request or something else, 
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def veggies_index(request):
    veggies = Veg.objects.all()
    return render(request, 'veggies/index.html', { 'veggies': veggies })

#this adds a new kind of vegetable to the store, does not include date, planted or stage
class VegCreate(CreateView):
    model = Veg
    fields = [ 'name', 'description', 'cost' ]
    success_url= '/veggies/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#there will be a seperate create to add instances of a vegetable to a garden

class InputList(ListView):
  model = Input

class InputDetail(DetailView):
  model = Input

class InputCreate(CreateView):
  model = Input
  fields = ['name', 'category', 'description', 'cost']
  success_url = '/inputs/'


class InputUpdate(UpdateView):
  model = Input
  fields = ['name', 'category', 'description', 'cost']
  success_url = '/inputs/'

class InputDelete(DeleteView):
  model = Input
  success_url = '/inputs/'

def inputs_index(request):
  inputs = Input.objects.all()
  return render(request, 'main_app/input_list.html', { 'inputs': inputs })




def veg_detail(request, veg_id):
    veg = Veg.objects.get(id=veg_id)
    return render(request, 'veggies/detail.html', { 'veg': veg })