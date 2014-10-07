from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    """ home view which servers the wiki home page """
    return render(request, 'home.html')
