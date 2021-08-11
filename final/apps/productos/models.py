from django.db import models

from apps.core.models import TimeModel
# Create your models here.

class Producto(TimeModel):
	nombre = models.CharField(max_length = 30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField(default = 0)
	

