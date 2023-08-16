import django_filters
from .models import Order


class OrderFilter(django_filters.FilterSet):
    # name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Order
        fields=['status',]