from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context = {}
    return render(request, 'welcome.html',context)

@login_required(login_url='/accounts/login/')
def index(request):
    context = {}
    return render(request,'index.html',context)
