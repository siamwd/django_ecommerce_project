from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from django.contrib.auth.decorators import login_required




def order_create(request):
    cart=None
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        
        if not cart or not cart.items.exists():
            return redirect("cart:cart_detail")
    
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            
            for item in cart.items.all():
                OrderItem.objects.create(
                    order = order,
                    product = item.product,
                    price = item.product.price,
                    quantity = item.quantity
                )
            cart.delete()
            del request.session["cart_id"]
            return redirect("orders:order_confirmation", order.id)
        else:
            form = OrderCreateForm()
            
        return render(request, "orders/order_create.html", {
            "cart":cart, "form":form
        })

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order_confirmation.html", {"order":order})

@login_required
def confirmed_orders(request):
    
    orders = Order.objects.all().order_by('-created_at')

    return render(request, "orders/confirmed_orders.html", {"orders": orders})
@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()  # DB থেকে delete
    return redirect("orders:confirmed_orders")
@login_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderCreateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders:confirmed_orders")
    else:
        form = OrderCreateForm(instance=order)

    return render(request, "orders/edit_order.html", {"form": form, "order": order})