from django.db import models
import shortuuid


# Create your models here.
class Quote(models.Model):

    class Meta:
        verbose_name_plural = 'Quotes'

    quote_ref = models.CharField(max_length=10, null=False, editable=False)
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
      blank=False)
    overall_weight = models.DecimalField(max_digits=7, decimal_places=2,
                                         null=False, blank=False)
    overall_volume = models.DecimalField(max_digits=7, decimal_places=2,
                                         null=False, blank=False)

    weight = models.DecimalField(
      help_text="Max 30kg's", max_digits=5, decimal_places=2,
      null=False, blank=False)
    height = models.DecimalField(max_digits=7, decimal_places=2,
                                 null=False, blank=False)
    width = models.DecimalField(max_digits=7, decimal_places=2,
                                null=False, blank=False)
    length = models.DecimalField(max_digits=7, decimal_places=2,
                                 null=False, blank=False)
    volume_weight = models.DecimalField(max_digits=7, decimal_places=2,
                                        null=False, blank=False)

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
    volume_weight1 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Volume Weight")

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
    volume_weight2 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Volume Weight")

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
    volume_weight3 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Volume Weight")

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
    volume_weight4 = models.DecimalField(
      max_digits=7, decimal_places=2, null=True, blank=True,
      default=0, verbose_name="Volume Weight")

    service = models.CharField(
      max_length=20, null=False, blank=False)
    spec_service = models.CharField(max_length=20, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    c_date = models.DateField(default="2012-09-04", null=True)
    d_date = models.DateField(default="2012-09-04", null=True)
    quote = models.DecimalField(max_digits=7, decimal_places=2,
                                null=False, default=0)

    @property
    def pound_amount(self):
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
        return self.d_postcode
