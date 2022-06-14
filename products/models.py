from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField
from django.core.exceptions import ValidationError


def size_line_validator(size_line: str):
    """Validate size_line field in Product's objects."""
    first_two = size_line[:2]
    second_two = size_line[3:]
    if (first_two + second_two).isdigit()\
            and size_line[2] == '-' \
            and int(first_two) <= int(second_two)\
            and (int(first_two) + int(second_two)) % 2 == 0:
        return size_line
    raise ValidationError('Size must contain "-" between sizes(both evens) '
                          'and first size '
                          'less than second, example: 42-50')


class Collection(models.Model):
    """Collection model, represents Product's category."""

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.title


class Product(models.Model):
    """Product model, represents Product objects."""

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

        """Define quantity_in_line."""
        first_two = self.size_line[:2]
        second_two = self.size_line[3:]
        self.quantity_in_line = (int(second_two) - int(first_two) + 2) // 2

        """Define an old_price if discount existing."""
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


