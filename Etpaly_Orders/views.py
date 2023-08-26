from django.shortcuts import render,get_object_or_404
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
    orders = Order.objects.all().order_by("-id")
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    # paginator = Paginator(orders, 10)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # Render a template with the records
    context = {'object_list': orders,
               'myfilter': myfilter}
    return render(request, 'Etpaly_Orders/ordersList.html', context)

def order_invoice(request, slug):
    # Retrieve a specific record by ID
    order = get_object_or_404(Order, slug=slug)
    context={'order':order}
    return render(request, 'Etpaly_Orders/invoice.html', context)


