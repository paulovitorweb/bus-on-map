from django.db import models
from django.contrib.gis.db import models as gismodels


class Route(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=32)
    geom = gismodels.LineStringField(srid=31985)

    def __str__(self):
        return f'{self.code} - {self.name}'