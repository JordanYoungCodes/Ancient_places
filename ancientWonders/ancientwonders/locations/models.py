from django.db import models
from django.urls import reverse

class Location(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    time_period = models.CharField(max_length=25)
    summary = models.CharField(max_length=120)
    main_image = models.ImageField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("loc_details", kwargs={"id":self.id})
    
    def get_absolute_url2(self):
        return reverse("loc_facts", kwargs={"id":self.id})

class Images(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    images = models.ImageField(blank=True)
    description = models.TextField(blank=True)


class FunFacts(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    factImage = models.ImageField(blank=True)
    factText = models.TextField(blank=True)


