from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
	context={}
	template='home.html'
	return render(request, template, context)

def about(request):
	context={}
	template='about.html'
	return render(request, template, context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def products(request):
	context={}
	template='products.html'
	return render(request, template, context)

def shoppingcart(request):
	context={}
	template='shoppingcart.html'
	return render(request, template, context)

def payments(request):
	context={}
	template='payments.html'
	return render(request, template, context)

def inventory(request):
	context={}
	template='inventory.html'
	return render(request, template, context)

def capacity(request):
	context={}
	template='capacity.html'
	return render(request, template, context)