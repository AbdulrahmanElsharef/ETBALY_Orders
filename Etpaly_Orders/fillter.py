import django_filters
from .models import Order,ORDER_STATUS


class OrderFilter(django_filters.FilterSet):
    customer__phone=django_filters.CharFilter(lookup_expr='icontains')
    customer__name=django_filters.CharFilter(field_name='customer',lookup_expr='icontains')
    code=django_filters.CharFilter(field_name='code',lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=ORDER_STATUS)    
    class Meta:
        model = Order
        fields=['code', 'status','customer__name',
                   'customer__phone']