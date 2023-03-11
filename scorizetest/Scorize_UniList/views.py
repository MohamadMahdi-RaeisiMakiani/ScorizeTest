from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import University_to_apply


class Show_All_Universities(ListView):
    model = University_to_apply
    context_object_name = 'all_uni'
    template_name = 'AllUnivercities_index.html'
    paginate_by = 3


class Show_University_Details(DetailView):
    model = University_to_apply
    context_object_name = 'one_uni'
    template_name = 'UniversityDetails_index.html'
