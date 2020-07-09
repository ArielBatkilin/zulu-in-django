from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import point

longitude = 37.7125
latitude =  38.7722

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = point
    context_object_name = 'zulu'
    queryset = point.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'zulu/index.html'
    
class addPoint(generic.ListView):
    model = point
    context_object_name = 'zulu'
    template_name = 'zulu/shit.html'

class PointList(generic.ListView):
    queryset = point.objects.filter(location__isnull=False)
    template_name = 'zulu/anotherMap.html'


