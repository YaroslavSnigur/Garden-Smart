from django.shortcuts import render
from django.http import HttpResponse
from .models import Veg, Input
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


class VegCreate(CreateView):
    model = Veg
    fields = [ 'name', 'description', 'cost', 'date', 'planted', 'stage' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
