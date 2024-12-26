from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='books/', blank=True, verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.title


class User(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return self.full_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    books = models.ManyToManyField(Book, through='OrderItem', verbose_name='Книги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'В ожидании'),
            ('completed', 'Завершён')
        ],
        default='pending',
        verbose_name='Статус'
    )
    order_key = models.CharField(max_length=20, unique=True, verbose_name='Ключ заказа')

    def __str__(self):
        return f"Заказ {self.id} ({self.user.full_name})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"
