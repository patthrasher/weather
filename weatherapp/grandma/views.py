from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib.request, json
from .forms import Weather_form
from .models import Weather

def index(request) :
    
    key = 'secret_key'

    if request.method == 'POST' :
        form = Weather_form(request.POST or None)

        if form.is_valid() :
            form.save()
            city = str(Weather.objects.last())
            city = city.replace(' ', '%20')

            service_url = 'http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + city
            print('service url:', service_url)


            response = urllib.request.urlopen(service_url)
            read = response.read()
            data = json.loads(read)

            f = data['current']['temp_f']

            print(f)
            context = {
                'x' : x,
                # 'api_address' : api_address,
                'key' : key,
                'place1' : place1,
                'place2' : place2,
                'city' : city,
                'f' : f,
            }

            return render(request, 'grandma/index.html', context)


    return render(request, 'grandma/index.html')
