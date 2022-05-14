from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/routes', views.routes, name='api_routes'),
    path('simulator', views.simulator, name='simulator')
]