from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    pending = orders.filter(status='Pending')
    delivered = orders.filter(status='Delivered')
    total_orders = orders.count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders, 'pending':pending, 'delivered':delivered}
    return render(request, 'accounts/home.html', context)

def product(request):
    return render(request, 'accounts/product.html')

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

def create_order(request, id):
    customer = Customer.objects.get(id=id)
    form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def update_order(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
