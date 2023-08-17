from django.shortcuts import render
from .models import Order
from django.views.generic import ListView
from .fillter import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
# class OrderList(ListView):
#     model = Order
    
#     def get_queryset(self):
#         data = Order.objects.filter(user=self.request.user)

#         return data
#     # total = Order.objects.aggregate(total=Sum('OrderDetail__get_total'))
#     # extra_context={'total':total}

def order_list(request):
    # Retrieve all records from the database
    orders = Order.objects.all()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    paginator = Paginator(orders, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Render a template with the records
    context = {'object_list': page_obj, 'count': Order.objects.all().count,
               'myfilter': myfilter}
    return render(request, 'Etpaly_Orders/order_list.html', context)


def dashboard_with_pivot(request):
    return render(request, 'Etpaly_Orders/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)