from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string

from .models import Book, OrderItem, Order, User

def index(request):
    return render(request,'index.html')


def books(request):
    all_books = Book.objects.all()
    return render(request, 'books.html', {'books': all_books})


def cart(request):
    cart_items = request.session.get('cart', {})
    books = []
    total_price = 0

    for book_id, quantity in cart_items.items():
        book = Book.objects.get(id=book_id)
        books.append({'book': book, 'quantity': quantity, 'total': book.price * quantity})
        total_price += book.price * quantity

    return render(request, 'cart.html', {'books': books, 'total_price': total_price})

def add_to_cart(request, book_id):
    cart = request.session.get('cart', {})
    cart[book_id] = cart.get(book_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def update_cart(request, book_id):
    cart = request.session.get('cart', {})
    action = request.GET.get('action')

    if action == 'increment':
        cart[book_id] = cart.get(book_id, 0) + 1
    elif action == 'decrement':
        if book_id in cart and cart[book_id] > 1:
            cart[book_id] -= 1
        else:
            cart.pop(book_id, None)

    request.session['cart'] = cart
    return redirect('cart')


def order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, 'order.html', {'message': 'Корзина пуста!'})

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        if not (full_name and email and address):
            return render(request, 'order.html', {'message': 'Все поля обязательны!'})

        # Создаём пользователя
        user = User.objects.create(full_name=full_name, email=email, address=address)

        # Создаём заказ
        order_key = get_random_string(10)
        order = Order.objects.create(user=user, status='pending', order_key=order_key)

        # Добавляем книги в заказ
        for book_id, quantity in cart.items():
            book = Book.objects.get(id=book_id)
            OrderItem.objects.create(order=order, book=book, quantity=quantity)

        # Очищаем корзину
        request.session['cart'] = {}

        return render(request, 'order.html', {'order_key': order_key, 'message': 'Заказ успешно оформлен!'})

    return render(request, 'order.html')
