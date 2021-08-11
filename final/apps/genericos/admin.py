from django.contrib import admin

# Register your models here.
from .models import Rubro, SubRubro

admin.site.register(Rubro)
admin.site.register(SubRubro)