from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = username
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username = username,email = email,password = password)
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'form':form,
        }
    return render(request,'registration/edit_profile.html',context)

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
