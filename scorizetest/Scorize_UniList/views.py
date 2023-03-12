from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import University_to_apply
from .filters import UniversityFilter


class Show_All_Universities(ListView):
    model = University_to_apply
    context_object_name = 'all_uni'
    template_name = 'AllUniversities_index.html'
    paginate_by = 3


class Show_University_Details(DetailView):
    model = University_to_apply
    context_object_name = 'one_uni'
    template_name = 'UniversityDetails_index.html'


class Show_Filtered_Universities(ListView):

    extra_context = {'choosed_country': "USA"}

    queryset = University_to_apply.objects.all()
    model = University_to_apply
    context_object_name = 'all_uni'
    template_name = 'FilteredUniversities_index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(Show_Filtered_Universities,
                        self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        self.srch = request.GET.get('search')
        global cntry
        cntry = request.GET.get('country')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            from_city__from_country__Country_Name__iexact=cntry).values()
        # if self.srch != "" or self.srch != None:
        #     queryset = super().get_queryset().filter(   __icontains=cntry).values()
        return queryset
    # def get_queryset(self):
    # queryset = super().get_queryset()
    # self.filterset = UniversityFilter(self.request.GET, queryset=queryset)
    # return self.filterset.qs

    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    # context['form'] = self.filterset
