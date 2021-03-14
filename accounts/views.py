from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request,'registration/signup.html',context)
