from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FormLogin, FormUserRegistration, FormProfile, FormUser
from .models import ModelProfile
from django.contrib import messages
from django.urls import reverse

# def login(request):
#     form_login = FormLogin()
    
#     if request.method == 'POST':
#         form_login = FormLogin(request.POST)
        
#         if form_login.is_valid():
#             cd = form_login.cleaned_data
#             user = authenticate(
#                 request,
#                 username=cd['username'],
#                 password=cd['password'])

#             if user:
#                 auth = True
#             if user.is_active:
#                 login(request, user)
#                 return redirect()
#             return render(request, 'account/login.html', {
#                 'form_login':form_login,
#                 'auth':auth
#                 })
#     return render(request, 'account/login.html', {'form_login':form_login})

@login_required
def profile(request):
    profile_avatar = request.user.profile.avatar
    profile_backround = request.user.profile.background

    if request.method == 'POST':
        form_profile = FormProfile(
            data=request.POST,
            instance=request.user.profile,
            files=request.FILES
            )
        form_user = FormUser(data=request.POST, instance=request.user)

        if form_profile.is_valid() and form_user.is_valid():
            form_profile.save()
            form_user.save()

            return redirect(reverse('account:profile'))
    else:
        form_profile = FormProfile(instance=request.user.profile)
        form_user = FormUser(instance=request.user)

        return render(request, 'account/profile.html', {
            'form_profile':form_profile,
            'form_user':form_user,
            'profile_avatar':profile_avatar,
            'profile_backround':profile_backround,
            })

def account(request, id):
    user = get_object_or_404(User, id=id, is_active=True)
    return render(request, 'account/account.html', {'user':user})

@login_required
def logout(request):
    django_logout(request)
    return redirect('/')

def registration(request):
    form = FormUserRegistration()

    if request.method == 'POST':
        form = FormUserRegistration(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            ModelProfile.objects.create(user=new_user)

            return render(request, 'registration/registration_done.html', {})

    return render(request, 'registration/registration.html', {'form':form})