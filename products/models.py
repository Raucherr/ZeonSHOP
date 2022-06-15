from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField
from django.core.exceptions import ValidationError


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
        help_text='Количество в линейке, создаётся атвтоматически '
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


