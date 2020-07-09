
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.

class point(models.Model):
    name = models.CharField(max_length=100)
    location = PointField()
    @property
    def lat_lng(self):
    	return list(getattr(self.location, 'coords', [])[::-1])
    discription = models.TextField()
