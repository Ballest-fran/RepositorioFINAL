from django.db import models

# Create your models here.
class Rubro(models.Model):
	nombre = models.CharField(max_length = 50)


class SubRubro(models.Model):
	nombre = models.CharField(max_length = 50)
	rubro = models.ForeignKey(Rubro, related_name = 'mi_rubro', on_delete=models.CASCADE)