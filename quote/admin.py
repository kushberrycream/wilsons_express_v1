from django.contrib import admin
from .models import Quote, Bookings


class QuoteAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('static/quote/css/quote_admin.css',),
        }
    search_fields = (
        "quote_ref__startswith", "c_postcode__startswith",
        "d_postcode__startswith"
    )

    readonly_fields = (
        'quote_ref', 'bookers_phone_number', 'bookers_email', 'date',
        'c_postcode', 'd_postcode', 'overall_weight', 'overall_volume',
        'height', 'length', 'width', 'weight', 'volume_weight',
        'quoted_price', 'height1', 'width1', 'length1', 'weight1',
        'volume_weight1', 'height2', 'width2', 'length2', 'weight2',
        'volume_weight2', 'height3', 'width3', 'length3', 'weight3',
        'volume_weight3', 'height4', 'width4', 'length4', 'weight4',
        'volume_weight4', 'service', 'spec_service',
    )

    list_display = (
        'quote_ref', 'c_postcode', 'd_postcode', 'date', 'overall_weight',
        'overall_volume', 'quoted_price'
    )

    fieldsets = (
        (None, {
            'fields': (
                'quote_ref', 'date', 'bookers_phone_number', 'bookers_email',
                'c_postcode', 'd_postcode', 'service', 'spec_service',
                'quoted_price', 'overall_weight', 'overall_volume',
            )
        }),
        ('Item 1', {
            'fields': ((
                'height', 'width', 'length', 'weight', 'volume_weight'),),
            'classes': ('required', 'thinner_labels', ),
        }),
        ('Item 2', {
            'fields': ((
                'height1', 'width1', 'length1', 'weight1', 'volume_weight1'),),
            'classes': ('required',),
        }),
        ('Item 3', {
            'fields': ((
                'height2', 'width2', 'length2', 'weight2', 'volume_weight2'),),
            'classes': ('required',),
        }),
        ('Item 4', {
            'fields': ((
                'height3', 'width3', 'length3', 'weight3', 'volume_weight3'),),
            'classes': ('required',),
        }),
        ('Item 5', {
            'fields': ((
                'height4', 'width4', 'length4', 'weight4', 'volume_weight4'),),
            'classes': ('required',),
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False


class BookingAdmin(admin.ModelAdmin):

    search_fields = (
        "booking_ref__startswith", "c_postcode__startswith",
        "d_postcode__startswith"
    )

    readonly_fields = (
        'booking_ref', 'bookers_phone_number', 'bookers_email', 'date',
        'c_postcode', 'd_postcode', 'overall_weight', 'overall_volume',
        'height', 'length', 'width', 'weight', 'volume_weight',
        'height1', 'width1', 'length1', 'weight1',
        'volume_weight1', 'height2', 'width2', 'length2', 'weight2',
        'volume_weight2', 'height3', 'width3', 'length3', 'weight3',
        'volume_weight3', 'height4', 'width4', 'length4', 'weight4',
        'volume_weight4', 'service', 'spec_service', 'price_gbp',
        'payment_complete', 'c_contact_name', 'c_company', 'c_phone_number',
        'c_street_address1', 'c_street_address2', 'c_town_or_city', 'c_county',
        'd_contact_name', 'd_company', 'd_phone_number',
        'd_street_address1', 'd_street_address2', 'd_town_or_city',
        'd_county',
    )

    list_display = (
        'booking_ref', 'c_postcode', 'd_postcode', 'date', 'overall_weight',
        'overall_volume', 'price_gbp', 'payment_complete'
    )

    fieldsets = (
        (None, {
            'fields': (
                'booking_ref', 'date', 'payment_complete',
                'bookers_phone_number', 'bookers_email',
                'service', 'spec_service', 'price_gbp',
                'overall_weight', 'overall_volume',),
            'classes': ('required', 'col-12'),
        }),
        ('Collection Address', {
            'fields': (
                'c_contact_name', 'c_company', 'c_phone_number',
                'c_street_address1', 'c_street_address2',
                'c_town_or_city', 'c_county', 'c_postcode'),
            'classes': ('required', 'col-lg-6'),
        }),
        ('Delivery Address', {
            'fields': (
                'd_contact_name', 'd_company', 'd_phone_number',
                'd_street_address1', 'd_street_address2', 'd_town_or_city',
                'd_county', 'd_postcode'),
            'classes': ('required', 'col-lg-6'),
        }),
        ('Item 1', {
            'fields': ((
                'height', 'width', 'length', 'weight', 'volume_weight'),),
            'classes': ('required', 'col-12'),
        }),
        ('Item 2', {
            'fields': ((
                'height1', 'width1', 'length1', 'weight1', 'volume_weight1'),),
            'classes': ('required', 'col-12'),
        }),
        ('Item 3', {
            'fields': ((
                'height2', 'width2', 'length2', 'weight2', 'volume_weight2'),),
            'classes': ('required', 'col-12'),
        }),
        ('Item 4', {
            'fields': ((
                'height3', 'width3', 'length3', 'weight3', 'volume_weight3'),),
            'classes': ('required', 'col-12'),
        }),
        ('Item 5', {
            'fields': ((
                'height4', 'width4', 'length4', 'weight4', 'volume_weight4'),),
            'classes': ('required', 'col-12'),
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Bookings, BookingAdmin)
admin.empty_value_display = '**Empty**'
