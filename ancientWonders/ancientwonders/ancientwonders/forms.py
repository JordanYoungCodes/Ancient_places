from django import forms
from locations.models import Location, Images, FunFacts
from django.forms import inlineformset_factory


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "location", "time_period", "summary", "main_image", "description"]

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["images", "description"]

class FunFactsForm(forms.ModelForm):
    class Meta:
        model = FunFacts
        fields = ["factImage", "factText"]


ImageFormSet = inlineformset_factory(
    Location, Images, fields=['images', 'description'], extra=1, can_delete=True
)

FactFormSet = inlineformset_factory(
    Location, FunFacts, fields=['factImage', 'factText'], extra=1, can_delete=True
)