from django.db import models


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)
    category_type = models.CharField(max_length=254, blank=True)
    description = models.TextField()
    image1_url = models.URLField(max_length=1024, blank=True)
    image1 = models.ImageField(blank=True)
    image2_url = models.URLField(max_length=1024, blank=True)
    image2 = models.ImageField(blank=True)
    image3_url = models.URLField(max_length=1024, blank=True)
    image3 = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:
        ordering = ('category',)

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True)
    box_qty = models.IntegerField(null=True, blank=True)
    per_roll = models.IntegerField(null=True, blank=True)
    image1_url = models.URLField(max_length=1024, blank=True)
    image1 = models.ImageField(blank=True)
    image2_url = models.URLField(max_length=1024, blank=True)
    image2 = models.ImageField(blank=True)

    def __str__(self):
        return self.name
