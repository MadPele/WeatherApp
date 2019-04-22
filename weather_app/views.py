from django.shortcuts import render
import requests


def index(request):

    city = request.GET.get('city', 'Wrocław')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=b6985db83abc6f18dce647a109fb20a4'

    data = requests.get(url).json()

    number = ((data['main']['temp'])-32)/1.8
    temperature = round(number,1)

    city_weather = {
        'city': city,
        'temperature': temperature,
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    context = {'city_weather' : city_weather}
    print(context)

    return render(request, 'weather_app/weather.html', context)
