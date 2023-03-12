from django_filters import FilterSet
from .models import University_to_apply


class UniversityFilter(FilterSet):
    class Meta:
        model = University_to_apply
        fields = {
            'Uni_Name': ['icontains']
        }
