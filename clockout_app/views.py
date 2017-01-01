from django.shortcuts import render
from .forms import DataForm

def home(request):
    form = DataForm()
    return render(request, 'clockout/home.html', {'form': form})