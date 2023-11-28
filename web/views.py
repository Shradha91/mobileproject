from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CustomUserCreationForm, ContactForm
from .models import Mobile

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'web/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'web/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return redirect('index')  # Replace 'index' with the desired URL name

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was submitted successfully!')
            return redirect('index')  # Redirect to a success page after saving
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form': form})


def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'web/mobiles.html', {'mobiles': mobiles})

def mobile_detail(request, slug):
    mobile = get_object_or_404(Mobile, slug=slug)
    return render(request, 'web/mobile_detail.html', {'mobile': mobile})

