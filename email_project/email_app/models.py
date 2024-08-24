from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('children', 'Дети'),
        ('teens', 'Подростки'),
        ('women', 'Женщины'),
        ('new_arrivals', 'Новинки'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    colors = models.ManyToManyField('Color', verbose_name="Цвета", blank=True)
    sizes = models.ManyToManyField('Size', verbose_name="Размеры", blank=True)
    characteristics = models.TextField(verbose_name="Характеристики", blank=True)
    care_instructions = models.TextField(verbose_name="Уход за изделием", blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Продукт")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.product.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Color(models.Model):
    COLOR_CHOICES = [
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('green', 'Зелёный'),
        ('yellow', 'Жёлтый'),
        ('black', 'Чёрный'),
        ('white', 'Белый'),
        ('pink', 'Розовый'),
        ('purple', 'Фиолетовый'),
        ('orange', 'Оранжевый'),
        ('grey', 'Серый'),
    ]

    name = models.CharField(max_length=20, choices=COLOR_CHOICES, verbose_name="Цвет", unique=True)  # Добавлено unique=True

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


# Модель для размера
class Size(models.Model):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]

    name = models.CharField(max_length=2, choices=SIZE_CHOICES, verbose_name="Размер")

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

# Модель для подписчика
class Subscriber(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    company_name = models.CharField(max_length=255, verbose_name="Название компании", blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email")
    date_subscribed = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
