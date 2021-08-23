import django_filters
from .models import Cards

class CardFilter(django_filters.FilterSet):
    # filter of name from description
    # the same names from models to do search of containt name
    # header = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cards
        # fields = '__all__'
        fields = ['description']
        # exclude = ['owner','category','language_type','image','code_blog','publish_at','slug']