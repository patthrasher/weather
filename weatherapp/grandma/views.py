from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import os
import urllib.request, json
from .forms import Weather_form
from .models import Weather


def index(request) :

    key = os.environ.get('weather_key')

    if request.method == 'POST' :
        form = Weather_form(request.POST or None)

        if form.is_valid() :
            form.save()
            last_city = str(Weather.objects.last())
            city = last_city.replace(' ', '%20')

            try :
                service_url = 'http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + city
                print('service url:', service_url)


                response = urllib.request.urlopen(service_url)
                read = response.read()
                data = json.loads(read)

                f = data['current']['temp_f']
                output = ''
                # f = 101
                if f >= 100 : output = 'swim suit'
                elif f >=  60 : output = 'tshirt'
                elif f >= 32 : output = 'coat'
                else : output = 'scarf'

                print(output)

                context = {
                'f' : f,
                'output' : output,
                'last_city' : last_city,
                }

                return render(request, 'grandma/index.html', context)

            except :
                messages.error(request, 'Hmm, we can\'t find that place, try another')
                return redirect('grandma:index')


    return render(request, 'grandma/index.html')
