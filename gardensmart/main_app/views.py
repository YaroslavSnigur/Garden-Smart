from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Veg, Input
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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


class VegCreate(CreateView):
    model = Veg
    fields = [ 'name', 'description', 'cost', 'date', 'planted', 'stage' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




def veg_detail(request, veg_id):
    veg = Veg.objects.get(id=veg_id)
    return render(request, 'veggies/detail.html', { 'veg': veg })