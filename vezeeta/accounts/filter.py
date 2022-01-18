import django_filters
from .models import Profile

class DoctorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Profile
        fields = ['doctor',"address","name"]
