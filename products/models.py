from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField


class Collection(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title





class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,
                                   related_name='collection')
    title = models.CharField(max_length=255)
    article = models.CharField(max_length=255, unique=True)
    actual_price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(default=None,
                                            null=True, blank=True)
    discount = models.PositiveIntegerField(default=None, null=True, blank=True)
    description = RichTextField()
    size_line = models.CharField(max_length=100)
    tissue_composition = models.CharField(max_length=250)
    quantity_in_line = models.PositiveIntegerField()
    material = models.CharField(max_length=100)
    bestseller = models.BooleanField(default=False)
    novelty = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
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