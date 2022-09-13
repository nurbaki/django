from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from decouple import config
import requests
from pprint import pprint
from .models import City
from django.contrib import messages

def home(request):
    api_key = config('api_key')
    user_city = request.GET.get('city')
    if user_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric'
        r = requests.get(url)
        if r.status_code == 200: # r.ok yazimi da ayni sonucu veriyor. yani boyle bir sehir/sayfa varmi diye kontrol ediyoruz
            content = r.json() # dictionary yani objeye ceviren fonksiyon
            r_city = content.get('name')
            if City.objects.filter(city=r_city):
                messages.warning(request, 'City already exists.')
            else:
                City.objects.create(city=r_city)
                messages.success(request, 'City succesfully created')
        else:
            messages.error(request, 'City does not exist')
    # city = 'Istanbul'
    cities = City.objects.all()
    city_data = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        r = requests.get(url)
        content = r.json() # dictionary yani objeye ceviren fonksiyon
        data = {
            'city': city,
            'temp': content.get('main').get('temp'),
            'description': content.get('weather')[0].get('description'),
            'icon': content.get('weather')[0].get('icon')
        }
        city_data.append(data)

    context = {
        'city_data' : city_data
    }    

    return render(request, 'wheatherapp/home.html', context)

def delete(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.success(request, 'City deleted')
    return redirect("home")
