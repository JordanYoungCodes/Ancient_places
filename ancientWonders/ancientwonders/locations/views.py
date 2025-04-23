from django.shortcuts import render, redirect
from .models import Location, Images, FunFacts
from django.views.generic.edit import CreateView, UpdateView
from ancientwonders.forms import LocationForm, ImagesForm, FunFactsForm, ImageFormSet, FactFormSet
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

def location_view(request):
    loc = Location.objects.all()
    return render(request, 'home.html', {'object': loc})



def detail_view(request, id):
    loc = Location.objects.get(id=id)
    imgs = Images.objects.filter(name=loc)

    return render(request, 'loc_details.html', {'object': loc, 'imgs':imgs})

def funfacts_view(request, id):
    loc = Location.objects.get(id=id)
    imgs = Images.objects.filter(name=loc)
    facts = FunFacts.objects.filter(name=loc)
    return render(request, 'fun_facts.html', {'loc':loc, 'imgs':imgs, 'facts':facts})

# class LocCreateView(View):
#     def get(self, request):
#         location_form = LocationForm()
#         images_form = ImagesForm()
#         facts_form = FunFactsForm()
#         return render(request, 'create_location.html', {
#             'location_form': location_form,
#             'images_form': images_form,
#             'facts_form': facts_form
#         })

#     def post(self, request):
#         location_form = LocationForm(request.POST, request.FILES)
#         images_form = ImagesForm(request.POST, request.FILES)
#         facts_form = FunFactsForm(request.POST, request.FILES)

#         if location_form.is_valid() and images_form.is_valid() and facts_form.is_valid():
#             location = location_form.save()

#             image = images_form.save(commit=False)
#             image.name = location  # ForeignKey link
#             image.save()

#             fact = facts_form.save(commit=False)
#             fact.name = location  # ForeignKey link
#             fact.save()

#             return redirect(location.get_absolute_url())
        
#         # If form is invalid, re-render the page with existing data
#         return render(request, 'create_location.html', {
#             'location_form': location_form,
#             'images_form': images_form,
#             'facts_form': facts_form
#         })

class LocCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'location_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        image_formset = ImageFormSet()
        fact_formset = FactFormSet()
        return render(request, self.template_name, {
            'form': form,
            'image_formset': image_formset,
            'fact_formset': fact_formset
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=location)
        fact_formset = FactFormSet(request.POST, request.FILES, instance=location)

        if form.is_valid() and image_formset.is_valid() and fact_formset.is_valid():
            location = form.save()
            image_formset.instance = location
            fact_formset.instance = location
            image_formset.save()
            fact_formset.save()
            return redirect(location.get_absolute_url())
        return render(request, self.template_name, {
            'form': form,
            'image_formset': image_formset,
            'fact_formset': fact_formset
        })



class LocUpdateView(View):
    template_name = 'location_form.html'  # Reuse the same form template

    def get(self, request, id):
        location = get_object_or_404(Location, id=id)
        form = LocationForm(instance=location)
        image_formset = ImageFormSet(instance=location)
        fact_formset = FactFormSet(instance=location)

        return render(request, self.template_name, {
            'form': form,
            'image_formset': image_formset,
            'fact_formset': fact_formset,
            'location': location
        })

    def post(self, request, id):
        location = get_object_or_404(Location, id=id)
        form = LocationForm(request.POST, request.FILES, instance=location)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=location)
        fact_formset = FactFormSet(request.POST, request.FILES, instance=location)

        if form.is_valid() and image_formset.is_valid() and fact_formset.is_valid():
            form.save()
            image_formset.save()
            fact_formset.save()
            return redirect(location.get_absolute_url())

        return render(request, self.template_name, {
            'form': form,
            'image_formset': image_formset,
            'fact_formset': fact_formset,
            'location': location
        })