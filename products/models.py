from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField


def size_line_validator(size_line: str):
    """Проверка поля size_line в объектах продукта."""
    first_two = size_line[:2]
    second_two = size_line[3:]
    if (first_two + second_two).isdigit()\
            and size_line[2] == '-' \
            and int(first_two) <= int(second_two)\
            and (int(first_two) + int(second_two)) % 2 == 0:
        return size_line
    raise ValidationError('Размер должен содержать "-" между размерами (оба события)'
                          'и первый размер '
                          'меньше второго, пример: 42-50)')


class Collection(models.Model):
    """Модель коллекции, представляющая категорию продукта."""

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.title


class Product(models.Model):
    """Модель продукта, представляющая объекты продукта."""

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,
                                   related_name='collection')
    title = models.CharField(max_length=255)
    article = models.CharField(max_length=255, unique=True)
    actual_price = models.PositiveIntegerField(
        help_text="Актуальная цена на данный момент.")
    old_price = models.PositiveIntegerField(
        help_text="Цена до скидки, создаётся атвтоматически "
                  "после указания скидки.",
        default=None, null=True, blank=True
                                            )
    discount = models.PositiveIntegerField(
        help_text="Скидка в процентах.",
        default=None, null=True, blank=True)
    description = RichTextField()
    size_line = models.CharField(max_length=5,
                                 validators=(size_line_validator,))
    tissue_composition = models.CharField(max_length=250)
    quantity_in_line = models.PositiveIntegerField(
        help_text='Количество в этой  линейке  создаётся атвтоматически '
                  'после линейки размеров.',
        blank=True)
    material = models.CharField(max_length=100)
    bestseller = models.BooleanField(default=False)
    novelty = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):

        """Определить количество в  строке."""
        first_two = self.size_line[:2]
        second_two = self.size_line[3:]
        self.quantity_in_line = (int(second_two) - int(first_two) + 2) // 2

        """Определите old_price, если скидка существует."""
        if self.discount is not None:
            self.old_price = self.actual_price
            self.actual_price = int(
                self.actual_price - (self.discount / 100 * self.actual_price)
            )
        super(Product, self).save(*args, **kwargs)


class ProductStyles(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_styles')
    color = RGBColorField()
    image = models.ImageField(blank=True, upload_to='images/')

    class Meta:
        verbose_name = "Товары по отдельности"
        verbose_name_plural = "Товары по отдельности"

    def __str__(self):
        return f"{self.product.title}   |   {self.color}    |   {self.image}"


class Cart(models.Model):
    """Корзина содержит все выбранные пользователем товары."""
    product = models.ForeignKey(ProductStyles, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f'{self.product.product.title} | {self.product.color}'


def calculate_order_info():
    """Вычисляет объекты корзины и возвращает кортеж деталей заказа."""
    lines_amount = Cart.objects.all().count()
    products_amount = sum(
        i.product.product.quantity_in_line *
        i.quantity for i in Cart.objects.all())
    total_price = sum(
        i.product.product.old_price * i.quantity for i in Cart.objects.all())
    actual_price = sum(
        i.product.product.actual_price * i.quantity for i in Cart.objects.all()
    )
    discount = total_price - actual_price
    return lines_amount, products_amount, total_price, actual_price, discount



ORDER_STATUSES = [
    ('НОВЫЙ', 'НОВЫЙ'),
    ('ОФОРМЛЕН', 'ОФОРМЛЕН'),
    ('ОТМЕНЕН', 'ОТМЕНЕН'),
]


class Order(models.Model):
    """Представляет собой объекты порядка."""

    '''Данные клиентов.'''
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField(unique=False)
    country = CountryField()
    city = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUSES,
                              default=ORDER_STATUSES[0][1],
                              auto_created=True)
    public_agreement = models.BooleanField(default=False)
    ordered_products = models.ManyToManyField(Cart)

    '''Рассчитать сумму заказа'''
    lines_amount = models.PositiveIntegerField(default=0)
    products_amount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    actual_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.lines_amount = calculate_order_info()[0]
        self.products_amount = calculate_order_info()[1]
        self.total_price = calculate_order_info()[2]
        self.actual_price = calculate_order_info()[3]
        self.discount = calculate_order_info()[4]
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.status




