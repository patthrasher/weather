from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    x = 'Grandmas got an index!'

    place1 = 'Austin'
    place2 = 'London'


    context = {
        'x' : x,
        'api_address' : api_address,
        'key' : key,
        'place1' : place1,
        'place2' : place2,
    }

    return render(request, 'grandma/index.html', context)
