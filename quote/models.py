from django.db import models


# Create your models here.
class Quote(models.Model):

    class Meta:
        verbose_name_plural = 'Quotes'

    delivery = models.CharField(max_length=8)
    collection = models.CharField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.delivery
