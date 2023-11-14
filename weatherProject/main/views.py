from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from django.urls import reverse 
import requests

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {
        'form': form
    })

@login_required
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        unit = request.POST.get('unit', 'metric')

        api_key = 'API_KEY_HERE'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        weather_data = {
            "country_code": data['sys']['country'],
            "coordinate": f"{data['coord']['lon']}, {data['coord']['lat']}",
            "temp": f"{data['main']['temp']} °{ 'F' if unit == 'imperial' else 'C'}",
            "pressure": data['main']['pressure'],
            "humidity": data['main']['humidity'],
            'main': data['weather'][0]['main'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return render(request, "main/index.html", {'weather_data': weather_data})
    else:
        return render(request, "main/index.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    user = request.user
    return render(request, 'main/home.html', {'user': user})