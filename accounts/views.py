from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='login_user')
def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login_user')
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

@login_required(login_url='login_user')
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

@login_required(login_url='login_user')
def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        messages.info(request, 'You deleted an order!')
        return redirect('home')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)

def create_customer(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'accounts/create_customer.html', context)
    return render(request, 'accounts/delete.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, 'Registration successful')
                return redirect('home')
        context = {'form': form}
        return render(request, 'registration/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Wrong username or password')
                return redirect('login_user')
        context = {}
        return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
