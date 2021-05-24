from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('booking', 'collection_postcode',
                       'delivery_postcode', 'items', 'lineitem_total',)
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_ref', 'user_profile', 'date', 'full_name',
                       'street_address1', 'street_address2',
                       'town_or_city', 'county', 'postcode',
                       'country', 'email', 'phone_number',
                       'order_total_format', 'vat', 'ten_percent_format',
                       'grand_total_format',
                       'stripe_pid')
    fieldsets = (
        (None, {
            'fields': (
                'order_ref', 'user_profile', 'date', 'full_name',
                'street_address1', 'street_address2',
                'town_or_city', 'county', 'postcode',
                'country', 'email', 'phone_number',
                'order_total_format', 'vat', 'ten_percent_format',
                'grand_total_format', 'stripe_pid',),
            'classes': ('required', 'col-12'),
        }),)

    list_display = ('order_ref', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Order, OrderAdmin)
