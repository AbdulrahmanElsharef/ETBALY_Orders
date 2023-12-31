import django_filters
from .models import Order,ORDER_STATUS,ORDER_Branch,Customer_Active


class OrderFilter(django_filters.FilterSet):
    customer__company=django_filters.CharFilter(lookup_expr='icontains')
    customer__client=django_filters.CharFilter(lookup_expr='icontains')
    customer__phone_1=django_filters.CharFilter(lookup_expr='icontains')
    customer__phone_2=django_filters.CharFilter(lookup_expr='icontains')
    customer__location=django_filters.CharFilter(lookup_expr='icontains')
    seller=django_filters.CharFilter(lookup_expr='icontains')
    designer=django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=ORDER_STATUS)  
    branch = django_filters.ChoiceFilter(choices=ORDER_Branch)  
    active = django_filters.ChoiceFilter(choices=Customer_Active)  

    class Meta:
        model = Order
        fields=[ 'id','branch','status','active','customer__company','customer__client',
                   'customer__phone_1','customer__phone_2','customer__location',"seller",'designer']

    