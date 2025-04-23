from django.contrib import admin
from .models import Location, Images, FunFacts

# Register your models here.
admin.site.register(Location)
admin.site.register(Images)
admin.site.register(FunFacts)