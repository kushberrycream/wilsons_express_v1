from django.db import models
import shortuuid
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Bookings(models.Model):

    class Meta:
        verbose_name_plural = 'Bookings'

    booking_ref = models.CharField(max_length=10, null=False, editable=False)
    d_postcode = models.CharField(
        max_length=8, verbose_name='Postcode', null=False,
        blank=False)
    c_postcode = models.CharField(
      max_length=8, verbose_name='Postcode',
      blank=False)
    overall_weight = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Actual Weight")
    overall_volume = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 1
    weight = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=False, blank=False,
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=False, blank=False)
    width = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, blank=False)
    length = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=False, blank=False)
    volume_weight = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 2
    weight1 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight1 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 3
    weight2 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight2 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 4
    weight3 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight3 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 5
    weight4 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight4 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    items = models.IntegerField(null=False, default=0)
    service = models.CharField(
      max_length=20, null=False, blank=False)
    spec_service = models.CharField(
      max_length=20, blank=False, verbose_name="Premium Service")
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=100, decimal_places=2,
                                null=False, default=0)
    bookers_email = models.EmailField(max_length=254,
                                      null=False, blank=False)
    bookers_phone_number = PhoneNumberField(
      verbose_name="Bookers Phone Number")
    d_contact_name = models.CharField(max_length=50, null=False, blank=False,
                                      verbose_name="Contact")
    d_company = models.CharField(max_length=100, blank=True,
                                 verbose_name="Company Name")
    d_email = models.EmailField(max_length=254, blank=True)
    d_phone_number = PhoneNumberField(verbose_name="Phone Number")
    d_street_address1 = models.CharField(
      max_length=80, null=False, blank=False, verbose_name="Address Line 1")
    d_street_address2 = models.CharField(max_length=80, blank=True,
                                         verbose_name="Address Line 2")
    d_town_or_city = models.CharField(max_length=40, null=False, blank=False,
                                      verbose_name="Town or City")
    d_county = models.CharField(max_length=80, blank=True,
                                verbose_name="County")
    c_contact_name = models.CharField(max_length=50, null=False, blank=False,
                                      verbose_name="Contact")
    c_company = models.CharField(max_length=100, blank=True,
                                 verbose_name="Company Name")
    c_email = models.EmailField(max_length=254, blank=True)
    c_phone_number = PhoneNumberField(verbose_name="Phone Number")
    c_street_address1 = models.CharField(
      max_length=80, null=False, blank=False, verbose_name="Address Line 1")
    c_street_address2 = models.CharField(max_length=80, blank=True,
                                         verbose_name="Address Line 2")
    c_town_or_city = models.CharField(max_length=40, null=False, blank=False,
                                      verbose_name="Town or City")
    c_county = models.CharField(max_length=80, blank=True,
                                verbose_name="County")
    date_booked = models.DateField(default=timezone.now, null=True)
    payment_complete = models.BooleanField(
      'Payment Complete', default=False,
      help_text=_("Only book once payment is complete!"))

    @property
    def price_gbp(self):
        return "£%s" % self.price if self.price else ""

    def __str__(self):
        return self.booking_ref


class Quote(models.Model):

    class Meta:
        verbose_name_plural = 'Quotes'

    quote_ref = models.CharField(max_length=10, null=False, editable=False)
    d_postcode = models.CharField(
        max_length=8, verbose_name='Delivery Postcode', null=False,
        blank=False)
    c_postcode = models.CharField(
      max_length=8, verbose_name='Collection Postcode',
      blank=False)
    overall_weight = models.CharField(
      max_length=12, blank=True, default=0, verbose_name="Actual Weight")
    overall_volume = models.CharField(
      max_length=12, blank=True, default=0, verbose_name="Volume Weight")
    # item 1
    weight = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=False, blank=False,
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=False, blank=False)
    width = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, blank=False)
    length = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=False, blank=False)
    volume_weight = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 2
    weight1 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length1 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight1 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 3
    weight2 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length2 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight2 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 4
    weight3 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length3 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight3 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    # item 5
    weight4 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight",
      validators=[MinValueValidator(0), MaxValueValidator(30)])
    height4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length4 = models.DecimalField(
      max_digits=10, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight4 = models.CharField(
      max_length=10, blank=True, default=0, verbose_name="Volume Weight")
    items = models.IntegerField(null=False)
    service = models.CharField(
      max_length=20, null=False, blank=False)
    spec_service = models.CharField(
      max_length=20, blank=False, verbose_name="Premium Service")
    date = models.DateTimeField(auto_now_add=True)
    quote = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, default=0)
    bookers_email = models.EmailField(max_length=254,
                                      null=False, blank=False)
    bookers_phone_number = PhoneNumberField()

    @property
    def quoted_price(self):
        return "£%s" % self.quote if self.quote else ""

    def _generate_quote_ref(self):
        """
        Generate a random, unique order ref using shortUUID
        """
        return shortuuid.ShortUUID(
            alphabet="013456789ABCDEFGHJKLMNPQRSTUVWXYZ").random(length=6)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order ref
        if it hasn't been set already.
        """
        if not self.quote_ref:
            self.quote_ref = self._generate_quote_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quote_ref
