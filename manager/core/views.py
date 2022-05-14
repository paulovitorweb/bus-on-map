from django.conf import settings
from django.http import HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from core.models import Route


def index(request):
    return render(request, 'core/index.html', {
        'OSM_TILE_LAYER': settings.OSM_CONFIG.get('TILE_LAYER'),
        'OSM_ATTRIBUTION': settings.OSM_CONFIG.get('ATTRIBUTION')
    })


def routes(request):
    return HttpResponse(serialize('geojson', Route.objects.all()))


def simulator(request):
    return render(request, 'core/gps_mock.html', {})
