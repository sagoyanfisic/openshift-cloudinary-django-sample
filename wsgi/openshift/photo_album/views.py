import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from cloudinary import api
from .models import Profile

def filter_nones(d):
    return dict((k,v) for k,v in d.iteritems() if v is not None)

def list(request):
    defaults = dict(format="jpg", height=150, width=150)

    samples = [
        dict(width = 120, height =120 ,
        crop = 'thumb', gravity = 'face',
        radius = 'max',  effect = ""),
    ]
    samples = [filter_nones(dict(defaults, **sample)) for sample in samples]
    return render(request, 'list.html', dict(photos=Profile.objects.all(), samples=samples))

