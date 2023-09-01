import django_filters
from .models import Order,ORDER_STATUS


class OrderFilter(django_filters.FilterSet):
    customer__name=django_filters.CharFilter(lookup_expr='icontains')
    customer__phone=django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=ORDER_STATUS)  

    class Meta:
        model = Order
        fields=[ 'id','status','customer__name',
                   'customer__phone']

    