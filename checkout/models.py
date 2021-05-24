import shortuuid

from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal

from quote.models import Bookings
from profiles.models import UserProfile


class Order(models.Model):
    order_ref = models.CharField(max_length=10, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2,
                              null=False, default=0)
    ten_percent_discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0,
        verbose_name="10% Discount")
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    @property
    def grand_total_format(self):
        return '£%s' % self.grand_total if self.grand_total else ''
    grand_total_format.fget.short_description = 'Grand Total'

    @property
    def order_total_format(self):
        return '£%s' % self.order_total if self.order_total else ''
    order_total_format.fget.short_description = 'Order Total'

    @property
    def ten_percent_format(self):
        return (
            '£%s' % self.ten_percent_discount
            if self.ten_percent_discount else ''
        )
    ten_percent_format.fget.short_description = '10% Discount'

    def _generate_order_ref(self):
        """
        Generate a random, unique order ref using shortUUID
        """
        return shortuuid.ShortUUID(
            alphabet="013456789ABCDEFGHJKLMNPQRSTUVWXYZ").random(length=10)

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.grand_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.vat = self.grand_total / Decimal(1.2)
        self.vat = self.grand_total - self.vat
        self.order_total = self.grand_total - self.vat
        if self.lineitems.count() >= settings.TEN_PERCENT_THRESHOLD:
            self.ten_percent_discount = (
                self.grand_total / 10
            )
        else:
            self.ten_percent_discount = 0
        self.grand_total = self.grand_total - self.ten_percent_discount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order ref
        if it hasn't been set already.
        """
        if not self.order_ref:
            self.order_ref = self._generate_order_ref()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_ref


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    booking = models.ForeignKey(
        Bookings, null=False, blank=False, on_delete=models.CASCADE)
    collection_postcode = models.CharField(
        max_length=10, blank=False, null=False)
    delivery_postcode = models.CharField(
        max_length=10, blank=False, null=False)
    items = models.CharField(max_length=1, blank=False, null=False)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.booking.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ref {self.booking.booking_ref} on order \
{self.order.order_ref}'
