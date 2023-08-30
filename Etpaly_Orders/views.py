from django.shortcuts import render,get_object_or_404
from .models import Order
from .fillter import *
from django.core.paginator import Paginator


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
    return render(request, 'Etpaly_Orders/orders_List.html', context)

def order_invoice(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Order, id=id)
    context={'order':obj}
    return render(request, 'Etpaly_Orders/invoice.html', context)


