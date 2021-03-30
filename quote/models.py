from django.db import models
import shortuuid
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
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
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    overall_volume = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    # item 1
    weight = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=False, blank=False)
    height = models.DecimalField(max_digits=7, decimal_places=2,
                                 null=False, blank=False)
    width = models.DecimalField(max_digits=7, decimal_places=2,
                                null=False, blank=False)
    length = models.DecimalField(max_digits=7, decimal_places=2,
                                 null=False, blank=False)
    volume_weight = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    # item 2
    weight1 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight")
    height1 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width1 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length1 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight1 = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    # item 3
    weight2 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight")
    height2 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width2 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length2 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight2 = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    # item 4
    weight3 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight")
    height3 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width3 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length3 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight3 = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")
    # item 5
    weight4 = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=True, blank=True, default=0, verbose_name="Weight")
    height4 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Height")
    width4 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Width")
    length4 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Length")
    volume_weight4 = models.CharField(
      max_length=7, blank=True, default=0, verbose_name="Volume Weight")

    service = models.CharField(
      max_length=20, null=False, blank=False)
    spec_service = models.CharField(
      max_length=20, blank=False, verbose_name="Premium Service")
    date = models.DateTimeField(auto_now_add=True)
    quote = models.DecimalField(max_digits=7, decimal_places=2,
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


class Booking(Quote):

    class Meta:
        verbose_name_plural = 'Bookings'

    booking_ref = models.ForeignKey(
      Quote, null=False, blank=False, on_delete=models.CASCADE,
      related_name="reference")
    d_contact_name = models.CharField(max_length=50, null=False, blank=False)
    d_company = models.CharField(max_length=100, blank=True)
    d_email = models.EmailField(max_length=254, null=False, blank=False)
    d_phone_number = PhoneNumberField()
    d_street_address1 = models.CharField(
      max_length=80, null=False, blank=False)
    d_street_address2 = models.CharField(max_length=80, blank=True)
    d_town_or_city = models.CharField(max_length=40, blank=True)
    d_county = models.CharField(max_length=80, blank=True)
    c_contact_name = models.CharField(max_length=50, null=False, blank=False)
    c_company = models.CharField(max_length=100, blank=True)
    c_email = models.EmailField(max_length=254, null=False, blank=False)
    c_phone_number = PhoneNumberField()
    c_street_address1 = models.CharField(
      max_length=80, null=False, blank=False)
    c_street_address2 = models.CharField(max_length=80, blank=True)
    c_town_or_city = models.CharField(max_length=40, blank=True)
    c_county = models.CharField(max_length=80, blank=True)
    date_booked = models.DateField(default=timezone.now, null=True)
    
    def __str__(self):
        return self.d_postcode
