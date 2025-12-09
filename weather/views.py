from django.shortcuts import render
import requests

def index(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '587af66001fb92f9eb85f3b28a4dea3a'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                'city': city.title(),
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'].title(),
                'country': response['sys']['country'],
                'humidity': response['main']['humidity'],
                'wind_speed': round(response['wind']['speed'] * 3.6, 1),  
                'icon': response['weather'][0]['icon'],
            }

    return render(request, 'index.html', {'weather': weather_data})
