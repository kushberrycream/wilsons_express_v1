from django.db import models


# Create your models here.
class Quote(models.Model):

    class Meta:
        verbose_name_plural = 'Quotes'

    d_contact_name = models.CharField(max_length=50, null=False, blank=False)
    d_company = models.CharField(max_length=100, blank=True)
    d_email = models.EmailField(max_length=254, null=False, blank=False)
    d_phone_number = models.CharField(max_length=20, null=False, blank=False)
    d_street_address1 = models.CharField(
      max_length=80, null=False, blank=False)
    d_street_address2 = models.CharField(max_length=80, blank=True)
    d_town_or_city = models.CharField(max_length=40, blank=True)
    d_county = models.CharField(max_length=80, blank=True)
    d_postcode = models.CharField(
        max_length=8, verbose_name='Delivery Postcode')
    c_contact_name = models.CharField(max_length=50, null=False, blank=False)
    c_company = models.CharField(max_length=100, blank=True)
    c_email = models.EmailField(max_length=254, null=False, blank=False)
    c_phone_number = models.CharField(max_length=20, null=False, blank=False)
    c_street_address1 = models.CharField(
      max_length=80, null=False, blank=False)
    c_street_address2 = models.CharField(max_length=80, blank=True)
    c_town_or_city = models.CharField(max_length=40, blank=True)
    c_county = models.CharField(max_length=80, blank=True)
    c_postcode = models.CharField(
        max_length=8, verbose_name='Collection Postcode')
    height = models.PositiveIntegerField(help_text="CMs")
    width = models.PositiveIntegerField(help_text="CMs")
    length = models.PositiveIntegerField(help_text="CMs")
    weight = models.DecimalField(
      help_text="KGs", max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.d_postcode
