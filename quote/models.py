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
        max_length=8, verbose_name='Delivery Postcode', null=False,
        blank=False)
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
      max_length=8, verbose_name='Collection Postcode',
      blank=True,)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    weight = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2)
    height1 = models.PositiveIntegerField(blank=True, null=False)
    width1 = models.PositiveIntegerField(blank=True, null=False)
    length1 = models.PositiveIntegerField(blank=True, null=False)
    weight1 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5,
      decimal_places=2, blank=True, null=False)
    height2 = models.PositiveIntegerField(blank=True, null=False)
    width2 = models.PositiveIntegerField(blank=True, null=False)
    length2 = models.PositiveIntegerField(blank=True, null=False)
    weight2 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5,
      decimal_places=2, blank=True, null=False)
    fragile = models.BooleanField(default=False, blank=True)
    security = models.BooleanField(default=False, blank=True)
    service = models.CharField(max_length=20, null=False, blank=False)
    spec_service = models.CharField(max_length=20, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    c_date = models.DateField(default="2012-09-04", null=True)
    d_date = models.DateField(default="2012-09-04", null=True)

    def __str__(self):
        return self.d_postcode
