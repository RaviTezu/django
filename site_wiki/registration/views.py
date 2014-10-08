from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Registration
from .forms import RegistrationForm

def register(request):
    """ register view which handles registration """ 
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            return HttpResponseRedirect('/thisworks/')
    else: 
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form,})
