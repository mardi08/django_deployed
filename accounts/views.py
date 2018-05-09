# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

import requests

# Create your views here.
def home(request):
    response = requests.get('http://api.ipstack.com/128.210.106.81?access_key=32cf0d458d472abe5b6cc3f45d6c20e5')
    geodata = response.json()
    return render(request, 'accounts/main.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'city': geodata['city'],
        'state': geodata['region_name'],
        'capital': geodata['location']['capital'],
        'language': geodata['location']['languages'][0]['native'],
    })
    # return render(request, 'accounts/main.html')
