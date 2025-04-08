from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def cart_view(request) -> HttpResponse:
    """
    Отображение страницы корзины пользователя.
    """
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('product')
    total_price = sum(item.product.price * item.quantity for item in items)

    return render(request, 'pages/cart.html', {
        'cart': cart,
        'items': items,
        'total_price': total_price,
    })


def add_to_cart(request, product_id: int) -> HttpResponseRedirect:
    """
    Добавляет товар в корзину.
    """
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')


def remove_from_cart(request, product_id: int) -> HttpResponseRedirect:
    """
    Удаляет товар из корзины.
    """
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('cart:cart_view')


def update_cart(request, product_id: int, action: str) -> HttpResponseRedirect:
    """
    Увеличивает или уменьшает количество товара в корзине.
    """
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('cart:cart_view')
