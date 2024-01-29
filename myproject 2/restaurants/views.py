from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm 
from .models import Dish,CartItem

def home(request): 
    return render(request, 'home.html')

def menu(request): 
    dishes = Dish.objects.all() 
    return render(request, 'menu.html', {'dishes': dishes})

def orders(request): 
    return render(request,'orders.html')

def location(request): 
    return render(request, 'location.html', )

def contact(request): 
    return render(request, 'contact.html',)

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.Dish.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, dish_id):
    if request.user.is_authenticated:
        Dish_item = Dish.objects.get(id=dish_id)
        cart_item, created = CartItem.objects.get_or_create(Dish=Dish_item,user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('orders')
    else:
        return redirect('login_user') 

 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('orders')



def login_user(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect('home') 
        else: 
            form = AuthenticationForm() 
            return render(request, 'login.html', {'form': form}) 
    else: 
        form = AuthenticationForm() 
        return render(request, 'login.html', {'form': form})

def logout_user(request): 
    logout(request) 
    return redirect('login_user')