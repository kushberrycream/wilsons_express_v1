from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Create_account(models.Model):
    class Meta:
        verbose_name = "account"
        verbose_name_plural = "Account Submissions"

    FREIGHT_TYPE = (
        ('mechanical', 'Mechanical'),
        ('plants_botanical', 'Plants and Botanical'),
        ('live_fish', 'Live Fish'),
        ('perishable', 'Perishable Items'),
        ('alcohol', 'Alcohol'),
        ('Other', 'Other Please Specify'),
    )

    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    company_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    freight = models.CharField(max_length=250, choices=FREIGHT_TYPE,
                               null=False, blank=False)
    other_comments = models.TextField(blank=True)
    complete = models.BooleanField(
      'Complete', default=False,
      help_text=_("Only Select Complete Once Account is 100% Set Up!"))

    def __str__(self):
        return self.full_name
